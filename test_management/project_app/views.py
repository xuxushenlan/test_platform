from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module
from django.forms.models import model_to_dict


# 项目管理
@login_required
def project_manage(request):
    username = request.session.get('user', '')
    project_list = Project.objects.all()
    return render(request, "project_manage.html", {"projects": project_list, "user": username})


@login_required
def module_manage(request):
    username = request.session.get('user', '')
    modules = Module.objects.all()
    module_list = []
    for module_ in modules:
        module_dict = model_to_dict(module_)
        module_dict["create_time"] = module_.create_time
        project_obj = Project.objects.get(pk=module_dict["project"])
        module_dict["project"] = project_obj.name
        module_list.append(module_dict)

    return render(request, "module_manage.html", {"modules": module_list, "user": username})
