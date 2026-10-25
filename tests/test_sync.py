import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import export_contract as contract
import sync

ONE = 'skl_' + 'a' * 22
TWO = 'skl_' + 'b' * 22
VERSION = 'skv_' + 'v' * 22
DATE = '2026-10-25T12:00:00Z'
NOW = datetime.fromisoformat(DATE.replace('Z', '+00:00')).timestamp()
OPAQUE = 'opaque.signature'


def encoded(value):
    return json.dumps(value, ensure_ascii=False).encode()


def entry(skill=ONE, title='Fix example', version=VERSION):
    return {'skill_id': skill, 'version_id': version, 'installation_name': 'fix-' + skill[-22:].lower(),
            'title': title, 'description': 'Example guidance', 'attribution': {'label': 'Original contributor', 'client': None},
            'published_at': DATE, 'version_sequence': '1', 'canonical_url': contract.ORIGIN + '/skills/' + skill,
            'exact_version_url': contract.ORIGIN + '/skills/' + skill + '/versions/' + version,
            'artifact_url': contract.ORIGIN + '/exports/skills/v1/artifacts/' + skill + '/' + version + '/SKILL.md',
            'source_snapshot_digest': 'a' * 64, 'public_input_digest': 'b' * 64, 'artifact_sha256': 'c' * 64, 'claim': OPAQUE}


def body(item, original='# Guidance\n\nOriginal body.\n'):
    metadata = {'skill_id': item['skill_id'], 'title': item['title'], 'version': item['version_id'],
                'updated': item['published_at'], 'canonical_url': item['canonical_url'],
                'author': item['attribution']['label'], 'terms': contract.ORIGIN + '/terms', 'artifact_format_revision': '2',
                'public_attribution': contract.canonical(item['attribution']), 'original_notices_and_references': '[{"notice":"Author rights"}]'}
    return ('---\nname: ' + json.dumps(item['installation_name']) + '\ndescription: ' + json.dumps(item['description'][:1024])
            + '\nmetadata:\n' + '\n'.join('  ' + k + ': ' + json.dumps(v) for k, v in metadata.items())
            + '\n---\n\n' + original + '\n\n---\n\nSource and original contributor rights.\n').encode()


class Service:
    def __init__(self, items=None, page_size=1):
        self.items = items if items is not None else [entry()]
        self.bodies = {}
        for item in self.items:
            self.bodies[item['skill_id']] = body(item)
            item['artifact_sha256'] = contract.sha256(self.bodies[item['skill_id']])
        self.page_size = page_size
        self.generation = '10'
        self.calls = []
        self.on_catalog = None
        self.on_validation = None
        self.on_artifact = None

    def snapshot(self):
        return {**contract.REVISIONS, 'snapshot_id': 'a' * 32, 'generation': self.generation, 'generated_at': DATE,
                'expires_at': '2026-10-25T18:00:00Z', 'page_size': self.page_size, 'expected_entry_count': len(self.items)}

    def fetch(self, url, body=None, limit=contract.JSON_LIMIT):
        self.calls.append((url, copy.deepcopy(body)))
        if url.startswith(contract.CATALOG):
            query = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
            offset = int(query.get('cursor', ['0.signature'])[0].split('.')[0])
            if self.on_catalog:
                result = self.on_catalog(offset)
                if result is not None:
                    return result
            count = min(len(self.items), offset + self.page_size)
            chain = contract.EMPTY_DIGEST
            for item in self.items[:count]:
                chain = contract.advance(chain, item)
            complete = count == len(self.items)
            return encoded({**self.snapshot(), 'entries': self.items[offset:count], 'selected_entry_count': count,
                            'manifest_digest': chain, 'complete': complete,
                            'next_cursor': None if complete else str(count) + '.signature',
                            'terminal_certificate': OPAQUE if complete else None})
        if url == contract.VALIDATE:
            offset = int(body.get('cursor', '0.signature').split('.')[0])
            if self.on_validation:
                result = self.on_validation(offset)
                if result is not None:
                    return result
            count = offset + len(body['claims'])
            complete = count == len(self.items)
            chain = contract.EMPTY_DIGEST
            for item in self.items[:count]:
                chain = contract.advance(chain, item)
            return encoded({'snapshot_id': 'a' * 32, 'generation': self.generation, 'complete': complete,
                            'selected_entry_count': count, 'manifest_digest': chain,
                            'next_cursor': None if complete else str(count) + '.signature',
                            'validation_receipt': OPAQUE if complete else None,
                            'validated_at': DATE if complete else None, 'expires_at': '2026-10-25T12:05:00Z' if complete else None})
        skill = urllib.parse.urlsplit(url).path.split('/')[-3]
        if self.on_artifact:
            result = self.on_artifact(skill)
            if result is not None:
                return result
        return self.bodies[skill]


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.service = Service()
        self.clock = patch('time.time', return_value=NOW)
        self.clock.start()
        self.addCleanup(self.clock.stop)
        self.git_patch = patch('sync.git', return_value='publisher-revision')
        self.git_patch.start()
        self.addCleanup(self.git_patch.stop)

    def run_sync(self, **kwargs):
        report = {}
        sync.run(self.root, fetch=self.service.fetch, workers=1, report=report, **kwargs)
        return report

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}

    def test_first_export_and_no_change_keep_exact_bytes_and_manifest(self):
        report = self.run_sync()
        self.assertEqual(report['status'], 'validated_not_published')
        self.assertEqual(report['artifacts_fetched'], 1)
        manifest = json.loads((self.root / 'skills.json').read_bytes())
        item = manifest['skills'][0]
        self.assertEqual((self.root / item['path']).read_bytes(), self.service.bodies[ONE])
        self.assertEqual(item['sha256'], contract.sha256(self.service.bodies[ONE]))
        self.assertNotIn('claim', json.dumps(manifest))
        before = self.snapshot()
        self.service.generation = '11'
        self.service.calls.clear()
        report = self.run_sync()
        self.assertEqual(report['artifacts_fetched'], 0)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(len(self.service.calls), 2)  # complete metadata and live admission

    def test_updates_preserve_server_installation_name_and_unowned_notes(self):
        self.run_sync()
        item = self.service.items[0]
        name = item['installation_name']
        note = self.root / 'skills' / name / 'note.txt'
        note.write_text('hand maintained')
        changed = entry(title='Completely changed title', version='skv_' + 'w' * 22)
        changed['installation_name'] = name
        self.service = Service([changed, entry(TWO)])
        self.run_sync()
        self.service = Service([entry(TWO)])
        self.run_sync()
        self.assertFalse((note.parent / 'SKILL.md').exists())
        self.assertEqual(note.read_text(), 'hand maintained')

    def test_failed_artifact_and_validation_leave_every_generated_file_unchanged(self):
        self.run_sync()
        before = self.snapshot()
        self.service = Service([entry(TWO)])
        self.service.on_artifact = lambda _skill: b'corrupt'
        with self.assertRaises(contract.ExportFailure):
            self.run_sync()
        self.assertEqual(before, self.snapshot())
        self.service.on_artifact = None
        self.service.on_validation = lambda _offset: (_ for _ in ()).throw(contract.ExportFailure('EXPORT_RESTRICTED'))
        report = {}
        with self.assertRaises(contract.ExportFailure):
            sync.run(self.root, fetch=self.service.fetch, report=report)
        self.assertEqual(report['status'], 'unsafe_stopped')
        self.assertEqual(before, self.snapshot())

    def test_corrupt_or_missing_local_artifact_is_repaired(self):
        self.run_sync()
        item = json.loads((self.root / 'skills.json').read_bytes())['skills'][0]
        path = self.root / item['path']
        for corrupt in (True, False):
            if corrupt:
                path.write_bytes(b'corrupt')
            else:
                path.unlink()
            self.assertEqual(self.run_sync()['artifacts_fetched'], 1)
            self.assertEqual(path.read_bytes(), self.service.bodies[ONE])

    def test_server_cannot_rename_existing_install(self):
        self.run_sync()
        before = self.snapshot()
        self.service.items[0]['installation_name'] = 'new-name'
        with self.assertRaisesRegex(contract.ExportFailure, 'rename'):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_unowned_paths_and_symlinks_are_never_overwritten(self):
        target = self.root / 'skills' / self.service.items[0]['installation_name'] / 'SKILL.md'
        target.parent.mkdir(parents=True)
        target.write_text('unowned')
        with self.assertRaisesRegex(contract.ExportFailure, 'unowned'):
            self.run_sync()
        target.unlink()
        outside = self.root / 'outside'
        outside.write_text('untouched')
        target.symlink_to(outside)
        with self.assertRaisesRegex(contract.ExportFailure, 'symlink'):
            self.run_sync()
        self.assertEqual(outside.read_text(), 'untouched')

    def test_empty_and_large_reductions_require_bound_review(self):
        self.run_sync()
        before = self.snapshot()
        self.service = Service([])
        selected = contract.catalog(self.service.fetch)
        with self.assertRaises(contract.ExportFailure) as caught:
            self.run_sync()
        binding = caught.exception.review_binding
        self.assertEqual(before, self.snapshot())
        wrong = {**binding, 'decision': 'approve', 'reason': 'Explained restriction', 'reviewed_by': 'Operator',
                 'evidence_url': 'https://github.com/Vectle/vectle/issues/843', 'manifest_digest': '0' * 64}
        with self.assertRaises(contract.ExportFailure):
            self.run_sync(review=wrong)
        review = {**wrong, **binding}
        self.run_sync(review=review)
        self.assertEqual(json.loads((self.root / 'skills.json').read_bytes())['skills'], [])
        # Nonzero large reductions preserve the original max(10, floor(n/10)).
        self.service = Service([entry('skl_' + f'{i:022d}') for i in range(30)])
        self.run_sync()
        self.service = Service(self.service.items[:19])
        with self.assertRaisesRegex(contract.ExportFailure, 'reduction'):
            self.run_sync()

    def test_obsolete_source_generation_is_rejected(self):
        self.run_sync()
        self.service.generation = '9'
        with self.assertRaisesRegex(contract.ExportFailure, 'Obsolete'):
            self.run_sync()

    def test_inventory_scan_is_read_only(self):
        report = self.run_sync(inventory_only=True)
        self.assertEqual(self.snapshot(), {})
        self.assertEqual(report['selected'], 1)
        self.assertEqual(report['status'], 'inventory_valid')
        self.assertEqual(len(self.service.calls), 1)

    def test_interrupted_download_preserves_repository(self):
        self.run_sync()
        before = self.snapshot()
        self.service = Service([entry(TWO)])
        self.service.on_artifact = lambda _skill: (_ for _ in ()).throw(KeyboardInterrupt())
        with self.assertRaises(KeyboardInterrupt):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_failure_never_advances_success_and_marks_stale(self):
        report = {'status': 'failed', 'ended_at': DATE}
        sync.write_report(report, last_success='2026-10-22T12:00:00Z')
        self.assertEqual(report['last_successful_check'], '2026-10-22T12:00:00Z')
        self.assertEqual(report['freshness'], 'stale')


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.service = Service([entry(), entry(TWO)])
        self.clock = patch('time.time', return_value=NOW)
        self.clock.start()
        self.addCleanup(self.clock.stop)

    def test_complete_pages_count_order_and_digest_then_validation(self):
        selected = contract.catalog(self.service.fetch)
        self.assertEqual(len(selected['entries']), 2)
        self.assertTrue(contract.validate(selected, self.service.fetch)['complete'])

    def test_actual_released_page_matches_contract_and_cross_language_digest(self):
        page = contract.decode((Path(__file__).parent / 'fixtures' / 'released-catalog-page.json').read_bytes())
        contract.check_snapshot(page, contract.instant(page['generated_at']))
        contract.check_entry(page['entries'][0])
        self.assertEqual(contract.advance(contract.EMPTY_DIGEST, page['entries'][0]), page['manifest_digest'])
        self.assertEqual(page['artifact_format_revision'], 2)

    def test_generation_restart_discards_partial_pages_and_is_bounded(self):
        failures = []
        def drift(offset):
            if offset:
                failures.append(offset)
                raise contract.ExportFailure('EXPORT_SNAPSHOT_CHANGED')
        self.service.on_catalog = drift
        with self.assertRaises(contract.ExportFailure):
            contract.catalog(self.service.fetch)
        self.assertEqual(failures, [1, 1, 1])
        self.service.on_catalog = None
        self.assertEqual(len(contract.catalog(self.service.fetch)['entries']), 2)

    def test_changed_generation_retries_validation_without_redownloading(self):
        self.service = Service([entry('skl_' + f'{i:022d}') for i in range(251)], page_size=250)
        selected = contract.catalog(self.service.fetch)
        failures = []
        def drift(offset):
            if offset and not failures:
                failures.append(offset)
                raise contract.ExportFailure('EXPORT_SNAPSHOT_CHANGED')
        self.service.on_validation = drift
        self.assertTrue(contract.validate(selected, self.service.fetch)['complete'])
        self.assertEqual(failures, [250])
        self.assertTrue(all(url == contract.VALIDATE or url.startswith(contract.CATALOG) for url, _body in self.service.calls))

    def test_malformed_partial_foreign_digest_and_revision_fail_closed(self):
        original = self.service.fetch
        for field, value in [('manifest_digest', '0' * 64), ('expected_entry_count', 0), ('complete', True),
                             ('schema_version', 2), ('artifact_format_revision', 1), ('name_map_revision', 'unknown'),
                             ('next_cursor', None), ('terminal_certificate', OPAQUE), ('selected_entry_count', 9),
                             ('expires_at', '2026-10-25T11:00:00Z')]:
            with self.subTest(field=field):
                def invalid(url, **kwargs):
                    result = json.loads(original(url, **kwargs))
                    result[field] = value
                    return encoded(result)
                with self.assertRaises(contract.ExportFailure):
                    contract.catalog(invalid)
        def foreign(offset):
            if offset:
                result = json.loads(Service.fetch(self.service, contract.CATALOG))
                result['snapshot_id'] = 'b' * 32
                return encoded(result)
        self.service.on_catalog = foreign
        with self.assertRaises(contract.ExportFailure):
            contract.catalog(self.service.fetch)

    def test_duplicate_ids_names_traversal_and_foreign_url_rejected(self):
        for key, value in [('skill_id', ONE), ('installation_name', self.service.items[0]['installation_name']),
                           ('installation_name', '../outside'), ('artifact_url', 'https://example.com/secret')]:
            with self.subTest(key=key, value=value):
                service = Service([entry(), entry(TWO)])
                service.items[1][key] = value
                with self.assertRaises(contract.ExportFailure):
                    contract.catalog(service.fetch)

    def test_duplicate_json_fields_and_oversized_response_rejected(self):
        for content in (b'{"entries":[],"entries":[]}', b' ' * (contract.JSON_LIMIT + 1)):
            with self.assertRaises(contract.ExportFailure):
                contract.decode(content)

    def test_transport_retries_are_five_bounded_and_foreign_origin_is_denied(self):
        import urllib.error
        from email.message import Message
        headers = Message()
        headers['Retry-After'] = '9999'
        unavailable = urllib.error.HTTPError(contract.CATALOG, 503, 'Unavailable', headers, None)
        with patch('urllib.request.build_opener') as opener, patch('time.sleep') as sleep:
            opener.return_value.open.side_effect = unavailable
            with self.assertRaisesRegex(contract.ExportFailure, 'retry_exhausted'):
                contract.request(contract.CATALOG)
            self.assertEqual(opener.return_value.open.call_count, 5)
            self.assertEqual([c.args[0] for c in sleep.call_args_list], [120] * 4)
        with patch('urllib.request.build_opener') as opener:
            with self.assertRaises(contract.ExportFailure):
                contract.request('https://example.com/exports/skills/v1/catalog')
            opener.assert_not_called()

    def test_hashed_artifact_still_requires_valid_spec_and_provenance(self):
        item = self.service.items[0]
        selected = contract.catalog(self.service.fetch)
        for content in [body({**item, 'installation_name': 'wrong'}), body({**item, 'attribution': {'label': 'Wrong', 'client': None}}), b'No frontmatter']:
            changed = {**item, 'artifact_sha256': contract.sha256(content)}
            with self.assertRaises(contract.ExportFailure):
                contract.artifact(changed, selected['terminal_certificate'], lambda _url, **_kwargs: content)

    def test_original_body_and_unicode_are_contiguous_and_unchanged(self):
        item = entry(title='Fix 🐝 café')
        original = '# Original\n\n```sh\necho café 🐝\n```\n'
        content = body(item, original)
        item['artifact_sha256'] = contract.sha256(content)
        result = contract.artifact(item, OPAQUE, lambda _url, **_kwargs: content)
        self.assertIn(original.encode(), result)

    def test_expired_or_foreign_validation_receipt_rejected(self):
        selected = contract.catalog(self.service.fetch)
        for key, value in [('snapshot_id', 'wrong'), ('manifest_digest', 'f' * 64),
                           ('expires_at', '2026-10-25T11:00:00Z'), ('selected_entry_count', 1),
                           ('validation_receipt', None)]:
            with self.subTest(key=key):
                def invalid(url, **kwargs):
                    result = json.loads(self.service.fetch(url, **kwargs))
                    result[key] = value
                    return encoded(result)
                with self.assertRaises(contract.ExportFailure):
                    contract.validate(selected, invalid)


class GitPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.remote = self.base / 'remote.git'
        self.root = self.base / 'checkout'
        subprocess.run(['git', 'init', '-q', '--bare', str(self.remote)], check=True)
        subprocess.run(['git', 'clone', '-q', str(self.remote), str(self.root)], check=True)
        sync.git(self.root, 'config', 'user.email', 'test@example.invalid')
        sync.git(self.root, 'config', 'user.name', 'Fixture')
        sync.git(self.root, 'checkout', '-b', 'main')
        self.service = Service()
        self.clock = patch('time.time', return_value=NOW)
        self.clock.start()
        self.addCleanup(self.clock.stop)
        # Prepare a validated initial catalog, then commit as the remote baseline.
        (self.root / 'README.md').write_text('Fixture publisher')
        sync.git(self.root, 'add', 'README.md')
        sync.git(self.root, 'commit', '-m', 'Fixture publisher')
        sync.run(self.root, fetch=self.service.fetch)
        sync.git(self.root, 'add', '.')
        sync.git(self.root, 'commit', '-m', 'Initial valid catalog')
        sync.git(self.root, 'push', 'origin', 'HEAD:main')

    def remote_head(self):
        return subprocess.check_output(['git', '--git-dir', str(self.remote), 'rev-parse', 'main'], text=True).strip()

    def test_no_change_does_not_commit_and_successful_update_is_one_commit(self):
        before = self.remote_head()
        result = sync.run(self.root, fetch=self.service.fetch, publish=True)
        self.assertEqual(result['status'], 'no_change')
        self.assertEqual(before, self.remote_head())
        self.service = Service([entry(), entry(TWO)])
        result = sync.run(self.root, fetch=self.service.fetch, publish=True)
        self.assertEqual(result['status'], 'published')
        self.assertEqual(sync.git(self.root, 'rev-parse', 'HEAD^'), before)
        self.assertEqual(self.remote_head(), result['new_commit'])
        self.assertFalse(result['install_verified'])

    def test_failed_push_keeps_remote_valid_and_retry_reconciles_without_force(self):
        before = self.remote_head()
        hook = self.remote / 'hooks' / 'pre-receive'
        hook.write_text('#!/bin/sh\nexit 1\n')
        hook.chmod(0o755)
        self.service = Service([entry(), entry(TWO)])
        with self.assertRaises(subprocess.CalledProcessError):
            sync.run(self.root, fetch=self.service.fetch, publish=True)
        self.assertEqual(before, self.remote_head())
        # The rejected run is intentionally discarded; a fresh clone is the retry.
        hook.unlink()
        retry = self.base / 'retry'
        subprocess.run(['git', 'clone', '-q', '-b', 'main', str(self.remote), str(retry)], check=True)
        sync.git(retry, 'config', 'user.email', 'test@example.invalid')
        sync.git(retry, 'config', 'user.name', 'Fixture')
        self.assertEqual(sync.run(retry, fetch=self.service.fetch, publish=True)['status'], 'published')

    def test_concurrent_branch_advance_stops_obsolete_publication(self):
        before = self.remote_head()
        advanced = []
        def racing(_skill):
            if not advanced:
                (self.root / 'README.md').write_text('Concurrent reviewed source change')
                sync.git(self.root, 'add', 'README.md')
                sync.git(self.root, 'commit', '-m', 'Concurrent source')
                sync.git(self.root, 'push', 'origin', 'HEAD:main')
                advanced.append(self.remote_head())
        self.service = Service([entry(), entry(TWO)])
        self.service.on_artifact = racing
        with self.assertRaisesRegex(contract.ExportFailure, 'advanced'):
            sync.run(self.root, fetch=self.service.fetch, publish=True)
        self.assertNotEqual(before, self.remote_head())
        self.assertEqual(self.remote_head(), advanced[0])
        self.assertEqual(len(json.loads((self.root / 'skills.json').read_bytes())['skills']), 1)


if __name__ == '__main__':
    unittest.main()
