from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from interface_app.forms import TestCaseForm
import requests
import json
from simplejson.errors import JSONDecodeError
from interface_app.models import TestCase
from project_app.models import Project, Module


def testcase(request):
    """
    获取用例列表
    """
    case_list = TestCase.objects.all()
    return render(request, "testcase_manage.html", {
        "cases": case_list,
        "type": "list",
        })


def add_case(request):
    """
    添加测试用例
    """
    form = TestCaseForm()

    if request.method == "POST":
        mid = request.POST['module_id']
        name = request.POST['name']
        url = request.POST['url']
        req_method = request.POST['req_method']
        parameter = request.POST['parameter']

        if mid == "" or name == "" or url == "" or req_method == "":
            return HttpResponse("必传参数为空")

        if parameter == "":
            parameter_dict = "{}"

        try:
            parameter_dict = json.loads(parameter.replace("'", "\""))
        except json.decoder.JSONDecodeError:
            return HttpResponse('接口参数格式错误, 必须字典形式{"id":1}')

        module_obj = Module.objects.get(pk=mid)

        TestCase.objects.create(name=name, module=module_obj, url=url, method=req_method,
                                parameter_body=parameter_dict)

        return HttpResponse("创建成功！")
    else:
        return render(request, "case_add.html", {
            "type": "add",
            "form": form,
        })


def api_debug(request):
    """
    接口调试
    """
    if request.method == "POST":
        url = request.POST['url']
        req_method = request.POST['req_method']
        parameter = request.POST['parameter']

        if parameter == "":
            parameter_dict = "{}"

        try:
            parameter_dict = json.loads(parameter.replace("'", "\""))
        except json.decoder.JSONDecodeError:
            return HttpResponse('接口参数格式错误, 必须字典形式{"id":1}')

        r = None
        if req_method == "get":
            r = requests.get(url, params=parameter_dict)

        if req_method == "post":
            r = requests.post(url, data=parameter_dict)

        if req_method == "put":
            r = requests.put(url, data=parameter_dict)

        if req_method == "delete":
            r = requests.delete(url, parameter_dict)

        try:
            print(r.json())
        except JSONDecodeError:
            return HttpResponse(r.text)

        # HistoryInterface.objects.create(
        #     name=name, url=url, type=req_method, parameter=parameter_dict)

        return HttpResponse(r.text)


def debug_case(request, cid):
    """
    调试测试用例
    """
    return render(request, "case_debug.html", {
        "type": "debug",
    })


def get_case_info(request):
    """
    获取用例信息
    """
    if request.method == "POST":
        case_id = request.POST.get("caseId", "")
        print(case_id)
        if case_id == "":
            return JsonResponse({"success":"false", "message":"case is null"})
        case_obj = TestCase.objects.get(pk=int(case_id))
        case_info = {
            "name": case_obj.name,
            "url": case_obj.url,
            "method": case_obj.method,
            "header": case_obj.header,
            "parameter_type": case_obj.parameter_type,
            "parameter_body": case_obj.parameter_body,
        }
        return JsonResponse({"success": "true", "message": "success", "data":case_info})
    else:
        return HttpResponse("404")
