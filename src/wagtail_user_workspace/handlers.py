from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.db.models import Model

from wagtail.models import GroupPagePermission

from allauth.account.signals import user_signed_up

from wagtail_user_workspace.utils import get_workspace_page_model

@receiver(user_signed_up, dispatch_uid="user_workspace_handler")
def create_user_workspace(sender, request=None, user=None, **kwargs):
    workspaces_page_model = get_workspace_page_model()
    user_workspace_model = workspaces_page_model.allowed_subpage_models()[0]
    try:
        workspaces_page = workspaces_page_model.objects.get()
    except Model.DoesNotExist as ex:    
        # TODO: Handle error and send message to user.
        raise RuntimeError("There is no Workspace Page! You should create one.") from ex

    #Create workspace page for new user    
    user_workspace = user_workspace_model(
        title = user.username + "'s workspace",        
        slug = user.username.replace("@", "_").replace(".", "_").replace("+", "_").replace("-", "_"), #replace chars that do not belong to slug        
        owner = user,        
    )

    workspaces_page.add_child(instance=user_workspace)

    # Create free plan user group, add edit permissions for users workspace page and add our new user to it.
    free_plan_group = Group.objects.get_or_create(name="Free plan - " + user.username)[0]

    free_plan_group.permissions.add(Permission.objects.get(codename="access_admin")) 

    GroupPagePermission.objects.create(group=free_plan_group, page=user_workspace, permission_type='add')
    GroupPagePermission.objects.create(group=free_plan_group, page=user_workspace, permission_type='edit')
    GroupPagePermission.objects.create(group=free_plan_group, page=user_workspace, permission_type='publish')

    user.groups.add(free_plan_group)