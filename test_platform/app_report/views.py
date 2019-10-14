import os
import time
import json
from xml.dom.minidom import parse

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.forms.models import model_to_dict

from test_platform import settings
from test_platform.common import response
from app_report.models import TestReport
from app_report.models import TestFile
from app_report.models import TestCase
from app_report.models import TestSnapshot
from app_report.utils import sort_file_by_time


# 测试报告目录
REPORT_DIR = settings.STATIC_DIR + "/static/report/"


def report_list(request):
    """
    返回报告页面
    """
    page_num = request.GET.get("page", "")

    reports = TestReport.objects.all()
    paginator = Paginator(reports, 10)

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
            "data_time": data.data_time,
            "error": data.error,
            "failure": data.failure,
            "skipped": data.skipped,
            "tests": data.tests,
            "run_time": data.run_time,
            "platform": data.platform,
            "version": data.version,
        }
        data_list.append(data_dict)

    return render(request, "report2.html", {"reports": reports, "page": page_data, "part": "report_list"})


def snapshot_list(request, rid):
    """
    查看报告截图列表
    """
    report = TestReport.objects.get(id=rid)
    snapshots = TestSnapshot.objects.filter(report=report)

    test_file_name = []
    for s in snapshots:
        test_file_name.append(s.test_file)
    test_file_name = list(set(test_file_name))

    data_list = []
    for i in range(len(test_file_name)):
        file_list = {"file_name": test_file_name[i], "id": i}
        cases = TestSnapshot.objects.filter(report=report, test_file=test_file_name[i])

        case_name_list = []
        for case in cases:
            case_name_list.append(case.test_case)
        case_name_list = list(set(case_name_list))

        case_list = []
        for case in case_name_list:
            steps = TestSnapshot.objects.filter(report=report, test_file=test_file_name[i], test_case=case).order_by('create_time')
            step_list = []
            for step in steps:
                step_list.append({"step": step.test_step, "name": step.name})

            case_list.append({
                "case_name": case,
                "step_list": step_list
            })

        file_list["case_list"] = case_list
        data_list.append(file_list)

    return render(request, "report2.html", {"report": report, "data_list": data_list, "part": "snapshot_list"})


def scan_report(request):
    """
    扫描报告目录，并写入TestReport表
    """
    if request.method == "GET":
        reports = TestReport.objects.all()
        names = []
        for r in reports:
            names.append(r.name)

        files = os.listdir(REPORT_DIR)
        for f_name in files:
            if f_name not in names:
                save_result(f_name)

        return response(message="同步报告完成！")
    else:
        return response(10101, "request method error")


def save_result(f_name):
    """
    读取junit-xml.xml文件中的结果，并保存TestReport表
    """
    platform = f_name.split("_")[0]
    version = f_name.split("_")[1]
    data_time = f_name.split("_")[2]
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data_time)))

    xml_report = os.path.join(REPORT_DIR, f_name, "junit-xml.xml")
    dom = parse(xml_report)

    root = dom.documentElement
    suite = root.getElementsByTagName('testsuite')

    errors = suite[0].getAttribute("errors")
    failures = suite[0].getAttribute("failures")
    skipped = suite[0].getAttribute("skipped")
    tests = suite[0].getAttribute("tests")
    run_time = suite[0].getAttribute("time")

    # 保存测试结果
    test_report = TestReport.objects.create(
        name=f_name,
        platform=platform,
        version=version,
        data_time=other_style_time,
        error=int(errors),
        failure=int(failures),
        skipped=int(skipped),
        tests=int(tests),
        run_time=float(run_time),
    )

    save_snapshots(test_report)


def save_snapshots(test_report):
    """
    保存报告截图
    :param test_report: 测试报告对象
    :return:
    """
    snapshot_path = os.path.join(REPORT_DIR, test_report.name, "snapshot")

    file_name_list = sort_file_by_time(snapshot_path)

    for file_name in file_name_list:
        name_part = file_name.split("::")
        test_file = name_part[0]
        test_case = name_part[-2].strip()
        test_step = time.strftime("%H:%M:%S", time.localtime(int(name_part[-1][:-4]) / 1000))

        try:
            tf = TestFile.objects.get(report=test_report, file_name=test_file)
        except TestFile.DoesNotExist:
            tf = TestFile.objects.create(report=test_report, file_name=test_file)

        try:
            tc = TestCase.objects.get(file=tf, case_name=test_case)
        except TestCase.DoesNotExist:
            tc = TestCase.objects.create(file=tf, case_name=test_case)

        try:
            TestSnapshot.objects.get(case=tc, full_path=file_name)
        except TestSnapshot.DoesNotExist:
            TestSnapshot.objects.create(case=tc, step_name=test_step, full_path=file_name)

    # 增加报告的描述
    save_case_desc(test_report)


def test(request):
    """测试"""
    if request.method == "GET":
        test_report = TestReport.objects.get(id=4)
        save_case_desc(test_report)
        return JsonResponse({"result": "ok"})
    else:
        return JsonResponse({"result": "fail"})


def save_case_desc(test_report):
    """
    保存测试用例的描述
    :param test_report: 测试报告对象
    :return:
    """
    case_desc = os.path.join(REPORT_DIR, test_report.name, "case.json")

    test_files = TestFile.objects.filter(report_id=test_report.id)
    file_ids = []
    for file in test_files:
        file_ids.append(file.id)

    cases_list = []
    for fid in file_ids:
        test_cases = TestCase.objects.filter(file_id=fid)
        for case in test_cases:
            cases_list.append({"id": case.id, "name": case.case_name})

    with(open(case_desc, "r")) as f:
        desc = f.read()
        case_desc_list = json.loads(desc)

    for case1 in case_desc_list:
        case_name = case1["case_name"].split("::")[-1]
        case_desc = case1["case_describe"]
        for case2 in cases_list:
            if case_name == case2["name"]:
                test_case = TestCase.objects.get(id=case2["id"])
                test_case.case_desc = case_desc
                test_case.save()


def report_preview(request, rid):
    """
    报告截图展示页面
    :param request:
    :param rid:
    :return:
    """
    if request.method == "GET":
        report = TestReport.objects.get(id=rid)
        report_name = report.name
        return render(request, "report_preview2.html", {"part": "preview", "report_name": report_name})


def case_tree(request, ):
    """
    测试用例列表
    :param request:
    :return:
    """
    if request.method == "GET":

        report_id = request.GET.get("rid", "")
        files = TestFile.objects.filter(report_id=report_id)
        data_list = []
        for file in files:
            file_dict = {
                "name": file.file_name,
                "isParent": True
            }

            cases = TestCase.objects.filter(file_id=file.id)
            case_list = []
            for case in cases:
                case_dict = {
                    "name": case.case_name,
                    "isParent": False,
                    "id": case.id,
                }

                case_list.append(case_dict)

            file_dict["children"] = case_list
            data_list.append(file_dict)

        return response(data=data_list)


def case_screenshots(request):
    """
    用例的截图
    """
    if request.method == "GET":
        cid = request.GET.get("cid", "")
        case = TestCase.objects.get(id=cid)

        snapshots = TestSnapshot.objects.filter(case_id=cid).order_by('create_time')
        snapshots_list = []
        for snap in snapshots:
            snapshots_list.append(model_to_dict(snap))

        return response(data={"desc": case.case_desc, "list": snapshots_list})



