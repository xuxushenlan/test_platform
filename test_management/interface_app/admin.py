from django.contrib import admin
from interface_app.models import TestCase


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'belong_project', 'belong_module', 'status'
    ,'url', 'mothod', 'header', 'parameter_type', 'parameter_body', 
    'response_assert', 'user']


admin.site.register(TestCase, TestCaseAdmin)
