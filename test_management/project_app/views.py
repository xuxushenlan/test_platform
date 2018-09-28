from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module
from django.forms.models import model_to_dict
from project_app.forms import AddProjectForm, AddModuleForm, PorjectForm
from django.views.generic.edit import UpdateView


# 项目管理
@login_required
def project_manage(request):
    username = request.session.get('user', '')
    project_list = Project.objects.all()
    return render(request, "project_manage.html", 
                 {"projects": project_list,
                  "user": username,
                  "type": "list",
                  })


# 添加项目
@login_required
def add_project(request):
    username = request.session.get('user', '')

    if request.method == 'POST':
        form = AddProjectForm(request.POST) # form 包含提交的数据
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = 1
            Project.objects.create(name=name,describe=describe, status=status)
            return HttpResponseRedirect('/manage/project/')

    else:
        form = AddProjectForm()

    return render(request, "project_manage.html", {"user": username, "form": form, "type": "add"})


# # 更新项目
# class ProjectUpdate(UpdateView):
#     model = Project
#     #form_class = AddProjectForm()
#     fields = ['name', 'describe', 'status']
#     template_name = 'project_manage.html'
#     #context_object_name = {"type": "edit"}


@login_required
def add_project(request):
    username = request.session.get('user', '')

    if request.method == 'POST':
        form = AddProjectForm(request.POST)  # form 包含提交的数据
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = 1
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/manage/project/')

    else:
        form = AddProjectForm()

    return render(request, "project_manage.html", {"user": username, "form": form, "type": "add"})


# 模块管理
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

    return render(request, "module_manage.html", {"modules": module_list, "user": username, "type": "list"})


# 添加模块
def add_module(request):
    username = request.session.get('user', '')
    if request.method == 'POST':
        form = AddProjectForm(request.POST)  #form 包含提交的数据
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = 1
            Project.objects.create(name=name, describe=describe, status=status)
            return HttpResponseRedirect('/manage/module/')

    else:
        form = AddModuleForm()

    return render(request, "module_manage.html", {"user": username, "form": form, "type": "add"})


def project(request, id=0):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = PorjectForm(request.POST)
        if form.is_valid():
            #id = form.data['id']
            if id:
                model = Project.objects.get(id=id)
            else:
                model = Project()
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
        id = 0
        return HttpResponseRedirect('/manage/project/')
    else:
        if id:
            form = PorjectForm(
                instance=Project.objects.get(id=id))
        else:
            form = PorjectForm()
    return render(request, 'project_manage.html', {
        'title': '变更记录',
        'form': form,  # 获得表单对象
        'data': Project.objects.all(),
        'id': id,
        'type': "edit"
    })
