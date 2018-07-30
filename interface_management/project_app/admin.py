from django.contrib import admin
from project_app.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time']


admin.site.register(Project, ProjectAdmin)
