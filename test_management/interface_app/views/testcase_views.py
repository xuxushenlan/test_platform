from django.shortcuts import render
from interface_app.models import TestCase
from django.http import HttpResponse
import requests
import json


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
    return render(request, "api_debug.html", {
        "type": "add",
    })


def debug_case(request, cid):
    """
    调试测试用例
    """
    return render(request, "api_debug.html", {
        "type": "debug",
    })


def api_debug(request):
    """
    接口调试动作
    """
    if request.method == "GET":
        name = request.GET['name']
        url = request.GET['url']
        req_method = request.GET['req_method']
        parameter = request.GET['parameter']

        if parameter == "":
            parameter_dict = "{}"

        try:
            parameter_dict = json.loads(parameter.replace("'", "\""))
        except JSONDecodeError2:
            return HttpResponse("参数格式错误")

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
