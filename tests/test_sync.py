import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync

ONE = "skl_" + "a" * 22
TWO = "skl_" + "b" * 22
DATE = "2026-10-10T02:00:00Z"
LATER = "2026-10-11T02:00:00Z"


def sitemap(items):
    return ('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + ''.join('<url><loc>' + sync.ORIGIN + '/skills/' + skill_id
                      + '</loc><lastmod>' + modified + '</lastmod></url>' for skill_id, modified in items)
            + '</urlset>').encode()


def payload(skill_id=ONE, title="Fix: example", version="skv_" + "v" * 22):
    return {"operation": "read_skill", "data": {
        "skill": {"skill_id": skill_id, "current_version_id": version}, "is_current": True,
        "version": {"skill_id": skill_id, "version_id": version, "title": title,
                    "description": "Example guidance", "markdown": "# Guidance\n\nOriginal body.\n",
                    "created_at": DATE, "author": {"label": "original-author"}}}}


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.discovery = [(ONE, DATE)]
        self.documents = {ONE: payload()}
        self.calls = []

    def fetch(self, url):
        self.calls.append(url)
        if url == sync.SITEMAP:
            return sitemap(self.discovery)
        document = self.documents[url.rsplit('/', 1)[-1]]
        if isinstance(document, Exception):
            raise document
        return json.dumps(document).encode()

    def run_sync(self):
        return sync.sync(self.root, self.fetch, workers=1)

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_first_export_and_unchanged_run_are_byte_identical(self):
        manifest = self.run_sync()
        item = manifest['skills'][0]
        text = (self.root / item['path']).read_text()
        self.assertIn('author: "original-author"', text)
        self.assertIn('canonical_url: "https://vectle.com/skills/' + ONE + '"', text)
        self.assertIn('Original body.', text)
        self.assertEqual(item['sha256'], hashlib.sha256(text.encode()).hexdigest())
        self.assertEqual(Path(item['path']).parent.name, item['name'])
        before = self.snapshot()
        self.calls.clear()
        self.run_sync()
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.calls, [sync.SITEMAP])

    def test_new_update_and_removal_preserve_installation_name_and_unowned_file(self):
        original = self.run_sync()['skills'][0]
        self.discovery = [(ONE, LATER), (TWO, DATE)]
        self.documents[ONE] = payload(title='Completely new title', version='skv_' + 'w' * 22)
        self.documents[TWO] = payload(TWO)
        updated = self.run_sync()
        first = next(item for item in updated['skills'] if item['skill_id'] == ONE)
        self.assertEqual(first['name'], original['name'])
        self.assertNotEqual(first['version'], original['version'])
        custom = (self.root / original['path']).parent / 'note.txt'
        custom.write_text('hand-maintained')
        self.discovery = [(TWO, DATE)]
        self.run_sync()
        self.assertFalse((self.root / original['path']).exists())
        self.assertEqual(custom.read_text(), 'hand-maintained')

    def test_a_failed_required_read_cannot_publish_partial_or_prune(self):
        self.run_sync()
        before = self.snapshot()
        self.discovery = [(TWO, DATE)]
        self.documents[TWO] = RuntimeError('public read unavailable')
        with self.assertRaises(RuntimeError):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_empty_or_malformed_discovery_cannot_delete_catalog(self):
        self.run_sync()
        before = self.snapshot()
        for xml in [sitemap([]), b'<urlset>', b'<sitemapindex/>', sitemap([(ONE, DATE), (ONE, DATE)]),
                    sitemap([('../outside', DATE)]), sitemap([(ONE, '2026-10-10')])]:
            with self.subTest(xml=xml), self.assertRaises((ValueError, sync.ET.ParseError)):
                sync.sync(self.root, lambda url: xml)
            self.assertEqual(before, self.snapshot())

    def test_wrong_version_or_nonpublic_read_is_rejected(self):
        for mutate in [lambda d: d['data'].update(is_current=False),
                       lambda d: d['data']['skill'].update(current_version_id='skv_' + 'z' * 22),
                       lambda d: d['data']['version'].update(skill_id=TWO),
                       lambda d: d.update(operation='search_network')]:
            document = payload()
            mutate(document)
            self.documents[ONE] = document
            with self.assertRaises(ValueError):
                self.run_sync()
            self.assertEqual(self.snapshot(), {})

    def test_corrupt_or_missing_generated_file_is_repaired(self):
        item = self.run_sync()['skills'][0]
        original = self.snapshot()
        path = self.root / item['path']
        path.write_text('edited by hand')
        self.run_sync()
        self.assertEqual(original, self.snapshot())
        path.unlink()
        self.run_sync()
        self.assertEqual(original, self.snapshot())

    def test_metadata_is_quoted_and_identical_titles_have_distinct_names(self):
        version = payload()['data']['version']
        version['title'] = '---\nname: injected\n" : $()'
        version['description'] = 'line1\n---\nname: injected'
        text = sync.render(version, sync.skill_name(version['title'], ONE))
        frontmatter = text.split('\n---\n', 1)[0].removeprefix('---\n')
        values = dict((key, json.loads(value)) for key, value in
                      (line.strip().split(': ', 1) for line in frontmatter.splitlines()
                       if line != 'metadata:'))
        self.assertEqual(values['description'], version['description'])
        self.assertEqual(values['title'], version['title'])
        self.assertLessEqual(len(values['name']), 64)
        self.assertNotEqual(sync.skill_name('Same title', ONE), sync.skill_name('Same title', TWO))

    def test_manifest_path_traversal_is_rejected(self):
        manifest = self.run_sync()
        manifest['skills'][0]['path'] = '../outside'
        (self.root / 'skills.json').write_text(json.dumps(manifest))
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_large_discovery_loss_cannot_prune_existing_files(self):
        manifest = self.run_sync()
        for number in range(100):
            item = copy.deepcopy(manifest['skills'][0])
            item['skill_id'] = 'skl_' + str(number).zfill(22)
            item['name'] = 'example-' + str(number)
            item['path'] = 'skills/' + item['name'] + '/SKILL.md'
            manifest['skills'].append(item)
        (self.root / 'skills.json').write_text(json.dumps(manifest))
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, '10%'):
            self.run_sync()
        self.assertEqual(before, self.snapshot())

    def test_quiet_catalog_has_only_one_keepalive_commit_per_month(self):
        with patch('sync.current_month', return_value='2026-10'):
            self.run_sync()
            before = self.snapshot()
            self.run_sync()
            self.assertEqual(before, self.snapshot())
        with patch('sync.current_month', return_value='2026-11'):
            self.run_sync()
        after = self.snapshot()
        self.assertEqual(before['skills.json'], after['skills.json'])
        self.assertNotEqual(before['sync-status.json'], after['sync-status.json'])


if __name__ == '__main__':
    unittest.main()
