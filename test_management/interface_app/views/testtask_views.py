from django.shortcuts import render
from interface_app.models import TestTask, TestCase


def testtask(request):
    """
    测试任务列表
    """
    task_list = TestTask.objects.all()
    return render(request, "testtask_manage.html", {
        "tasks": task_list,
        "type": "list",
        })


def add_test_cases(request):
    """
    添加用例
    """
    case_list = TestCase.objects.all()
    return render(request, "testtask_manage.html", {
        "cases": case_list,
        "type": "add_case",
    })
