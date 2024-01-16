from django.core.exceptions import ImproperlyConfigured

from wagtail_user_workspace.settings import settings
from wagtail_user_workspace.utils import get_workspace_page_model

def check_workspace_model_configured():
    if settings.USER_WORKSPACE_PAGE_MODEL is None:
        raise ImproperlyConfigured("USER_WORKSPACE_PAGE_MODEL is not configured! Provide model class of page that should serve as a workspace page.")

def check_workspace_model_type():
    from wagtail.models import Page

    workspace_model = get_workspace_page_model()

    if not issubclass(workspace_model, Page):
        raise ImproperlyConfigured("USER_WORKSPACE_PAGE_MODEL is not Wagtail Page! Workspace Page should be subclass of Wagtail's Page model.")

def check_subpge_types_count():
    workspace_model = get_workspace_page_model()    
    subpage_models_count = len(workspace_model.allowed_subpage_models())

    if subpage_models_count is not 1:
        raise ImproperlyConfigured(
            "Workspace page model {model_name} can have only one subpage_type entry, but has {subpage_models_count}!"
            .format(
                model_name = workspace_model.__name__,
                subpage_models_count = subpage_models_count
            )
        )