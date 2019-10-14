import time
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from test_platform.settings import BASE_DIR
from app_performance.config import URL, USER, PAWD
from app_performance.models import TestData


def performance(request):
    """
    性能管理主页面
    """
    test_data = TestData.objects.filter(status=True).order_by('-pushed_time')

    paginator = Paginator(test_data, 10)
    page_num = request.GET.get('page', "")
    if page_num == "":
        page_num = 1

    try:
        contacts = paginator.page(page_num)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    page_data = {
        "number": contacts.number,
        "has_previous": contacts.has_previous,
        "previous_page_number": contacts.previous_page_number,
        "has_next": contacts.has_next,
        "next_page_number": contacts.next_page_number,
        "num_pages": contacts.paginator.num_pages
    }

    data_list = []
    for data in contacts:
        data_dict = {
            "id": data.id,
            "device": data.device,
            "pushed_time": data.pushed_time,
            "app": data.app,
            "app_version": data.app_version,
            "cpu_avg": round(data.cpu_usage_avg, 2),
            "mem_avg": data.mem_usage_avg,
            "mem_max": data.mem_usage_max,
            "fps_median": data.fps_median,
            "fps_stability": round(data.fps_stability),
        }
        data_list.append(data_dict)

    return render(request, "performance.html", {"data": data_list, "page": page_data})


def delete_data(request, data_id):
    """
    删除数据
    """
    test_data = TestData.objects.get(id=data_id)
    test_data.status = False
    test_data.save()
    return HttpResponseRedirect("/")


def get_data(request):
    """
    获取 gamebatch 数据
    """

    # results = get_gamebench_data()

    with open(BASE_DIR + "/data.json", "r") as f:
        ret_json = json.loads(f.read())
        results = ret_json["results"]

    test_data = TestData.objects.all()
    test_list = []
    for d in test_data:
        test_list.append(d.session_id)

    for ret in results:
        time_str = str(ret["timePushed"])[0:10]

        datetime_format = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime(int(time_str)))

        sid = ret["id"]
        device = ret["device"]["name"]
        app = ret["app"]["name"]
        version = ret["app"]["version"]

        if ret["metrics"]["cpu"] is True:
            cpu_usage_avg = float(ret["cpuUsageAvg"])
            cpu_usage_median = float(ret["cpuUsageMedian"])
            cpu_usage_min = float(ret["cpuUsageMin"])
            cpu_usage_max = float(ret["cpuUsageMax"])
        else:
            cpu_usage_avg = float(0)
            cpu_usage_median = float(0)
            cpu_usage_min = float(0)
            cpu_usage_max = float(0)

        if ret["metrics"]["memory"] is True:
            mem_usage_avg = int(ret["memUsageAvg"])
            mem_usage_median = int(ret["memUsageMedian"])
            mem_usage_min = int(ret["memUsageMin"])
            mem_usage_max = int(ret["memUsageMax"])
        else:
            mem_usage_avg = int(0)
            mem_usage_median = int(0)
            mem_usage_min = int(0)
            mem_usage_max = int(0)

        if ret["metrics"]["fps"] is True:
            fps_min = int(ret["fpsMin"])
            fps_max = int(ret["fpsMax"])
            fps_median = int(ret["fpsMedian"])
            fps_stability = float(ret["fpsStability"])
        else:
            fps_min = int(0)
            fps_max = int(0)
            fps_median = int(0)
            fps_stability = float(0)

        # 添加数据库没有的记录
        if ret["id"] not in test_list:
            TestData.objects.create(session_id=sid,
                                    device=device,
                                    app=app,
                                    app_version=version,
                                    pushed_time=datetime_format,
                                    cpu_usage_avg=cpu_usage_avg,
                                    cpu_usage_median=cpu_usage_median,
                                    cpu_usage_min=cpu_usage_min,
                                    cpu_usage_max=cpu_usage_max,
                                    mem_usage_avg=mem_usage_avg,
                                    mem_usage_median=mem_usage_median,
                                    mem_usage_min=mem_usage_min,
                                    mem_usage_max=mem_usage_max,
                                    fps_min=fps_min,
                                    fps_max=fps_max,
                                    fps_median=fps_median,
                                    fps_stability=fps_stability
                                    )

    return HttpResponseRedirect("/manage_page")


def get_gamebench_data():
    """
    內部方法：获取gamebench 服务平台数据。
    :return:
    """
    requests.adapters.DEFAULT_RETRIES = 3
    session = requests.Session()
    session.keep_alive = False
    headers = {'Connection': 'close'}
    # 实现登录
    login_user = {"username": USER, "password": PAWD, "from": "web"}
    ret = session.post(URL + "Auth/login", json=login_user, headers=headers)
    result = ret.json()
    token = result["token"]

    # 获所有测试的概要数据
    headers2 = {'Authorization': 'JWT ' + token}
    ret = session.get(URL + "sessions?page=0&pageSize=15&sort=timePushed:desc", headers=headers2)
    result = ret.json()
    results = result["results"]
    return results

