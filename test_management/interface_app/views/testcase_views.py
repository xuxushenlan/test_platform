from django.shortcuts import render
from interface_app.models import TestCase


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
    return render(request, "testcase_manage.html", {
        "type": "add",
    })


def debug_case(request, cid):
    """
    调试测试用例
    """
    return render(request, "testcase_manage.html", {
        "type": "debug",
    })
