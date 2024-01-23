
import os

from django import setup
from django.test import TestCase, override_settings
from django.core.exceptions import ImproperlyConfigured

from wagtail_user_workspace.checks import check_workspace_model_type, check_workspace_model_configured, check_subpge_types_count

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.config.dev"
setup()

class ChecksTestCase(TestCase):

    @override_settings(USER_WORKSPACE_PAGE_MODEL="tests.InvalidWorkspacePage")
    def test_check_workspace_model_type_invalid(self):
        self.assertRaises(ImproperlyConfigured,check_workspace_model_type)

    @override_settings(USER_WORKSPACE_PAGE_MODEL=None)
    def test_check_workspace_model_configured_invalid(self):
        self.assertRaises(ImproperlyConfigured, check_workspace_model_configured)

    @override_settings(USER_WORKSPACE_PAGE_MODEL="tests.ToManySubpageTypesWorkspacePage")
    def test_check_subpge_types_count_to_many(self):
        self.assertRaises(ImproperlyConfigured, check_subpge_types_count)

    @override_settings(USER_WORKSPACE_PAGE_MODEL="tests.ZeroSubpageTypesWorkspacePage")
    def test_check_subpge_types_count_zero(self):
        self.assertRaises(ImproperlyConfigured, check_subpge_types_count)