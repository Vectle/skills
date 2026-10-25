import contextlib
import inspect
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync


class WorkerConfigurationTests(unittest.TestCase):
    def test_workflow_uses_bounded_choice_and_quoted_environment_value(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/sync.yml').read_text()
        dispatch = workflow.split('  workflow_dispatch:\n', 1)[1].split('  push:\n', 1)[0]
        self.assertIn('      artifact_workers:\n', dispatch)
        self.assertIn('        type: choice\n', dispatch)
        self.assertIn("        default: '2'\n", dispatch)
        self.assertIn("        options: ['1', '2', '3', '4']\n", dispatch)
        self.assertIn("ARTIFACT_WORKERS: ${{ github.event.inputs.artifact_workers || '2' }}", workflow)
        self.assertIn('--workers "$ARTIFACT_WORKERS"', workflow)
        self.assertIn('timeout-minutes: 300', workflow)
        self.assertIn('cancel-in-progress: false', workflow)

    def test_cli_defaults_and_choices_remain_bounded_before_any_work(self):
        self.assertEqual(inspect.signature(sync.run).parameters['workers'].default, 2)
        self.assertEqual(inspect.signature(sync.stage).parameters['workers'].default, 2)
        for workers in [None, '1', '2', '3', '4']:
            args = ['sync.py'] + (['--workers', workers] if workers else [])
            with patch.object(sys, 'argv', args), patch.object(sync, 'run') as run, patch.object(sync, 'write_report'):
                sync.main()
                self.assertEqual(run.call_args.kwargs['workers'], int(workers or 2))
        for workers in ['0', '5', 'invalid']:
            with patch.object(sys, 'argv', ['sync.py', '--workers', workers]), patch.object(sync, 'run') as run:
                with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                    sync.main()
                self.assertEqual(error.exception.code, 2)
                run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
