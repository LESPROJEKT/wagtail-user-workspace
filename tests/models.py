from django.db import models
from wagtail.models import Page
from wagtail_user_workspace.models import WorkspacePageBase

class BasicPage1(Page):
    pass

class BasicPage2(Page):
    pass


class InvalidWorkspacePage(WorkspacePageBase, models.Model):
    pass

class ValidWorkspacePage(WorkspacePageBase, Page):
    subpage_types = [
        'tests.BasicPage1',
    ]

class ToManySubpageTypesWorkspacePage(WorkspacePageBase, Page):
    subpage_types = [
        'tests.BasicPage1',
        'tests.BasicPage2',
    ]

class ZeroSubpageTypesWorkspacePage(WorkspacePageBase, Page):
    subpage_types = []