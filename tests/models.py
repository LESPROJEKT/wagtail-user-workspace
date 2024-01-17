from django.db import models
from wagtail.models import Page
from wagtail_user_workspace.models import WorkspacePageBase
from coderedcms.models import CoderedWebPage

class WebPage(CoderedWebPage):
    
    class Meta:
        verbose_name = "Web Page"

    template = "coderedcms/pages/web_page.html"

class ValidWorkspacePage(WorkspacePageBase, CoderedWebPage):    

    subpage_types = [
        'tests.WebPage',
    ]

    template = "coderedcms/pages/web_page.html"

#Private models used only in tests
#Cannot be created from editor interface
    
class NonCreatablePageMixin:
    parent_page_types = []

class BasicPage1(Page, NonCreatablePageMixin):
    pass

class BasicPage2(Page, NonCreatablePageMixin):
    pass

class InvalidWorkspacePage(WorkspacePageBase, models.Model, NonCreatablePageMixin):    
    pass

class ToManySubpageTypesWorkspacePage(WorkspacePageBase, Page, NonCreatablePageMixin):    
    subpage_types = [
        'tests.BasicPage1',
        'tests.BasicPage2',
    ]

class ZeroSubpageTypesWorkspacePage(WorkspacePageBase, Page, NonCreatablePageMixin):    
    subpage_types = []