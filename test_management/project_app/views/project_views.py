from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module
from django.forms.models import model_to_dict
from project_app.forms import AddProjectForm, ProjectForm
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


@login_required
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
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
        form = ProjectForm()

    return render(request, "project_manage.html", {"user": username, "form": form, "type": "add"})


@login_required()
def edit_project(request, pid):
    """
    编辑更新项目
    :param request:
    :param pid: 项目ID
    :return:
    """
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            if pid:
                model = Project.objects.get(id=pid)
            else:
                model = Project()
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.status = form.cleaned_data['status']
            model.save()
        return HttpResponseRedirect('/manage/project/')
    else:
        if pid:
            form = ProjectForm(
                instance=Project.objects.get(id=pid))
        else:
            form = ProjectForm()
    return render(request, 'project_manage.html', {
        'title': '变更记录',
        'form': form,  # 获得表单对象
        'data': Project.objects.all(),
        'id': pid,
        'type': "edit"
    })


@login_required
def delete_project(request, pid):
    """
    删除项目
    :param request:
    :param pid: 项目ID
    :return:
    """
    Project.objects.get(id=pid).delete()
    return HttpResponseRedirect("/manage/project")


