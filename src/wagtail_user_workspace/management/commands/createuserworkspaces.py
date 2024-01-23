from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from wagtail_user_workspace.handlers import create_user_workspace
from wagtail_user_workspace.utils import get_workspace_page_model

class Command(BaseCommand):
    help = 'Generates user workspace pages for users that has none.'   

    def handle(self, *args, **options):
       workspaceless_users = self.get_users_without_workspace()

       if workspaceless_users.count() < 1:
           self.stdout.write("No users without workspace.")
           return
       else:
           self.stdout.write("Added workspaces:")
           self.stdout.write("-----------------")

       for user in workspaceless_users:
           create_user_workspace(None, None, user)
           self.stdout.write(user.username + "'s workspace")

    def get_users_without_workspace(self):
        workspaces_parent = get_workspace_page_model().objects.get()

        return User.objects.exclude(id__in=workspaces_parent.get_children().values("owner_id"))