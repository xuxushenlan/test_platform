from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module


# 项目管理
@login_required
def project_manage(request):
    username = request.session.get('user', '')
    project_list = Project.objects.all()
    return render(request, "project_manage.html", {"projects": project_list, "user": username})


@login_required
def module_manage(request):
    username = request.session.get('user', '')
    return render(request, "module_manage.html", {"user": username})
