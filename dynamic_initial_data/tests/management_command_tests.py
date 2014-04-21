from django.core.management import call_command
from django.test import TestCase
from mock import patch


class SyncInitialDataTest(TestCase):
    """
    Tests each of the management commands
    """
    def test_no_arguments(self):
        """
        Makes sure the sync_initial_data method gets called when the command is run
        """
        with patch('dynamic_initial_data.base.InitialDataManager.update_all_apps') as update_patch:
            call_command('sync_initial_data')
            self.assertEqual(1, update_patch.call_count)
