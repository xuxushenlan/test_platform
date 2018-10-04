from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module
from django.forms.models import model_to_dict
from project_app.forms import ProjectForm, ModuleForm
from django.views.generic.edit import UpdateView


@login_required
def module_manage(request):
    """
    模块管理
    :param request:
    :return:
    """
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


def add_module(request):
    """
    添加模块
    :param request:
    :return:
    """
    username = request.session.get('user', '')
    if request.method == 'POST':
        form = ModuleForm(request.POST)  #form 包含提交的数据
        if form.is_valid():
            project_name = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project_obj = Project.objects.get(name=project_name)
            Module.objects.create(name=name, describe=describe, project_id=int(project_obj.id))
            return HttpResponseRedirect('/manage/module/')
    else:
        form = ModuleForm()

    return render(request, "module_manage.html", {"user": username, "form": form, "type": "add"})


@login_required()
def edit_module(request, mid):
    """
    编辑更新模块
    :param request:
    :param pid: 模块ID
    :return:
    """
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            if mid:
                model = Module.objects.get(id=mid)
            else:
                model = Module()
            model.name = form.cleaned_data['name']
            model.describe = form.cleaned_data['describe']
            model.project = form.cleaned_data['project']
            model.save()
        return HttpResponseRedirect('/manage/module/')
    else:
        if mid:
            form = ModuleForm(
                instance=Module.objects.get(id=mid))
        else:
            form = ModuleForm()
    return render(request, 'module_manage.html', {
        'title': '变更记录',
        'form': form,  # 获得表单对象
        'data': Module.objects.all(),
        'id': mid,
        'type': "edit"
    })


@login_required
def delete_module(request, mid):
    """
    删除模块
    :param request:
    :param mid: 模块ID
    :return:
    """
    Module.objects.get(id=mid).delete()
    return HttpResponseRedirect("/manage/module")

