import json
import requests
from test_management import common
from interface_app.models import TestCase
from project_app.models import Project, Module
from django.forms.models import model_to_dict

def get_project_list(request):
    """
    获取项目模块列表
    """
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            project_dict = {
                "name": project.name
            }
            module_list = Module.objects.filter(project_id=project.id)
            if len(module_list) != 0:
                module_name = []
                for module in module_list:
                    module_name.append(module.name)

                project_dict["moduleList"] = module_name
                data_list.append(project_dict)

        return common.response_succeed(data=data_list)

    else:
        return common.response_failed("请求方法错误")


def get_case_list(request):
    """
    获取单个模块的用例列表
    """
    if request.method == "POST":
        project_name = request.POST.get("pName", "")
        module_name = request.POST.get("mName", "")

        if project_name == "" or module_name == "":
            return common.response_failed("项目或模块名称不能为空")
        try:
            project_obj = Project.objects.get(name=project_name)
        except Project.DoesNotExist:
            return common.response_failed("项目查询失败")
        try:
            module_obj = Module.objects.get(name=module_name, project_id=project_obj.id)
        except Module.DoesNotExist:
            return common.response_failed("模块查询失败")

        testcase_list = TestCase.objects.filter(module=module_obj)
        cases_list = []
        for case in testcase_list:
            cases_list.append(model_to_dict(case))
        return common.response_succeed(data=cases_list)

    else:
        return common.response_failed("请求方法错误")


def get_cases_list(request):
    """
    获取所有用例的例表
    """
    if request.method == "GET":
        projects = Project.objects.all()

        cases_list = []
        for project in projects:
            modules = Module.objects.filter(project_id=project.id)
            for module in modules:
                cases = TestCase.objects.filter(module_id=module.id)
                for case in cases:
                    case_info = {
                        "porject": project.name,
                        "module": module.name,
                        "caseId": case.id,
                        "caseName": case.name, 
                    }
                    cases_list.append(case_info)
        print(cases_list)     
        return common.response_succeed(message="用例列表", data=cases_list)
    else:
        return common.response_failed("请求方法错误")
