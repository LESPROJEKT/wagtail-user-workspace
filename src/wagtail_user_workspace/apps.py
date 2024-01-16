from django.apps import AppConfig
from wagtail_user_workspace.checks import check_workspace_model_configured, check_workspace_model_type, check_subpge_types_count

class WagtailUserWorkspaceConfig(AppConfig):    
    default_auto_field = 'django.db.models.BigAutoField'
    name = "wagtail_user_workspace"    

    def ready(self) -> None:
        from wagtail_user_workspace import handlers

        check_workspace_model_configured()
        check_workspace_model_type()
        check_subpge_types_count()

        return super().ready()