import os
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from interface_app.models import TestTask, TestCase
from interface_app.apps import TASK_RUN_FILE, TASK_PATH
from interface_app.extend.file import mkdir


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


# 运行任务
def run_task(request, tid):
    if request.method == "GET":
        task_obj = TestTask.objects.get(id=tid)
        cases_list = task_obj.cases.split(",")
        task_obj.status = 1     # 更新状态为运行中
        task_obj.save()
        task_id_path = TASK_PATH + str(tid)
        # mkdir(task_id_path)   # 创建任务目录

        cases_dict = {}
        for case_id in cases_list:
            if case_id == "":
                continue
            else:
                case_obj = TestCase.objects.get(id=int(case_id))
                print("id", case_obj.id)
                case_dict = {
                    "url": case_obj.url,
                    "method": case_obj.req_method,
                    "type": case_obj.req_type,
                    "header": case_obj.req_header,
                    "parameter": case_obj.req_parameter,
                    "assert_text": case_obj.resp_assert,
                }
                cases_dict[case_obj.id] = case_dict

        cases_str = json.dumps(cases_dict)
        cases_data_file = TASK_PATH + "/case_data.json"
        with(open(cases_data_file, 'w')) as f:
            f.write(cases_str)

        # run_cases()  # 运行函数
        print(TASK_RUN_FILE)
        os.system("python " + TASK_RUN_FILE)
        
        return HttpResponseRedirect("/interface/task_manage")
    else:
        return HttpResponse("404")

# 如何去运行这些用例？--单元测试框架 + 数据驱动

# unittest + ddt
