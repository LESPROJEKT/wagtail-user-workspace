from django.apps import apps

from wagtail_user_workspace.settings import settings

def get_workspace_page_model():
    return apps.get_model(settings.USER_WORKSPACE_PAGE_MODEL)