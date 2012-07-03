# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.contrib import admin

from mezzanine.core import admin as core_admin

from mezzanine.pages import admin as pages_admin

from categorylink import models

from copy import deepcopy

from django import forms

CATEGORY_LINK_FIELDSETS = deepcopy(pages_admin.PageAdmin.fieldsets)
CATEGORY_LINK_FIELDSETS[0][1]['fields'].insert(1, 'blog_category')


class CategoryLinkForm(forms.ModelForm):
    class Meta:
        model = models.CategoryLink


class CategoryLinkAdmin(pages_admin.PageAdmin): #, core_admin.StackedDynamicInlineAdmin):
    form = CategoryLinkForm
    fieldsets = CATEGORY_LINK_FIELDSETS

admin.site.register(models.CategoryLink, CategoryLinkAdmin)

# EOF

