import os

from django import setup
from django.contrib.auth import get_user_model
from wagtail.test.utils import WagtailPageTestCase
from wagtail.test.utils.form_data import nested_form_data, streamfield
from wagtail_user_workspace.utils import get_workspace_page_model
from wagtail_user_workspace.handlers import create_user_workspace

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.config.dev"
setup()

class TestCreateuserworkspacesCommand(WagtailPageTestCase):
    fixtures = ["users_workspaces_page_deleted.json"]

    def test_user_role_granted_workspace_page_permission_after_regeneration(self):
        # Load premade user from fixture
        user = get_user_model().objects.get(username="user1")

        # Recreate his workspace page
        create_user_workspace(None, None, user)
        workspace_page = get_workspace_page_model().objects.get().get_children().get(owner=user)

        # Check it's creation and permissions
        self.assertIsNot(workspace_page, None, msg="No page was created!")
        self.assertPageIsEditable(
            page=workspace_page,
            user=user,
            # post_data=self.post_data,
            msg="User {user} can't edit his {workspace_page} page!".format(user=user.get_username(), workspace_page=workspace_page.title))      