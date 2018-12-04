from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from interface_app.models import TestCase
from interface_app.models import TestTask

"""
说明：接口任务文件，返回HTML页面
"""

# 获取任务列表
def task_manage(request):
    testtasks = TestTask.objects.all()
    
    if request.method == "GET":
        return render(request, "task_manage.html", {
            "type": "list",
            "testtasks": testtasks,
        })
    else:
        return HttpResponse("404")


# 创建任务
def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", {
            "type": "add",
        })
    else:
        return HttpResponse("404")

# 运行测试任务
def run_task(request, tid):
    if request.method == "GET":
        task_obj = TestTask.objects.get(id=tid)
        cases_str = task_obj.cases
        cases_list = cases_str.split(",")
        print("666", cases_list)
        for i in cases_list:
            try:
                int(i)
            except ValueError:
                continue
            else:
                case_obj = TestCase.objects.get(id=i)
                print(case_obj.name)
        
        return HttpResponseRedirect('/interface/task_manage')

    else:
        return HttpResponse("404")
