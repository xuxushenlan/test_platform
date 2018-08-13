from django.contrib import admin
from project_app.models.project_models import Project
from project_app.models.module_models import Module

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
