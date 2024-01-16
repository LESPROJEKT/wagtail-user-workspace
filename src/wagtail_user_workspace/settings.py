from django.conf import settings as django_settings

# All attributes accessed with this prefix are possible to overwrite
# through django.conf.settings.
settings_prefix = "USER_WORKSPACE_"

class Settings:
    USER_WORKSPACE_PAGE_MODEL = None

    def __getattribute__(self, __name: str):
        """
        Check if a Django project settings should override the app default.

        In order to avoid returning any random properties of the django settings, we inspect the prefix firstly.
        """
        if __name.startswith(settings_prefix) and hasattr(django_settings, __name):
            return getattr(django_settings, __name)

        return super().__getattribute__(__name)
    
    def __setattr__(self, __name, __value) -> None:
        raise RuntimeError("Settings cannot be changed during runtime!")

settings = Settings()
