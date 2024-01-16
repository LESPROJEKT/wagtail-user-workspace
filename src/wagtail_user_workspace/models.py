from django.db import models

from solo.models import SingletonModel

class WorkspacePageBase(SingletonModel):
    #This is a little bit dirty workaround. Default is 1 which causes that the Root page is overwritten by this page. And that breaks Wagtail...
    singleton_instance_id = 999999999   

    class Meta:
        abstract = True
