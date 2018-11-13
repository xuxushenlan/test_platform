from django.contrib import admin
from interface_app.models import TestCase, TestTask


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'module', 'status'
    ,'url', 'method', 'header', 'parameter_type', 'parameter_body', 
    'response_assert', 'create_user']


class TestTaskAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "status", "api_id"]

admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestTask, TestTaskAdmin)
