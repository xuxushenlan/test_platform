import json
import logging
import requests
from django.http import JsonResponse
from django.http import QueryDict
from app_mock.models import MockData
from test_platform import common
from test_platform import settings

logger = logging.getLogger('stu')


def del_api(request):
    """
    删除Api
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        data = MockData.objects.get(id=mid)
        data.delete()
        return common.response(message="删除成功")
    else:
        return common.response_method_error()


def edit_api(request):
    """
    编辑Api
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        data = MockData.objects.get(id=mid)
        desc = data.desc
        return common.response(message="获取成功", data=desc)
    else:
        return common.response_method_error()


def save_api(request):
    """
    保存Api
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        desc = request.POST.get("desc", "")

        data = MockData.objects.get(id=mid)
        data.desc = desc
        data.save()
        return common.response(message="保存成功")
    else:
        return common.response_method_error()


def update_api(request):
    """
    同步Api返回结果
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        data = MockData.objects.get(id=mid)

        url = "http://{env}.klook.io/{uri}".format(env=data.env, uri=data.uri)
        logger.info('url:{path} method:{method} URL:{url}'.format(path=request.path, method=request.method, url=url))
        if data.method == "get":
            r = requests.get(url)
        elif data.method == "post":
            r = requests.post(url)
        else:
            r = {}

        if r.status_code != 200:
            return common.response(10102, "同步失败！检查{env} 环境是否正常".format(env=data.env))
        else:
            data.response = r.text
            data.save()
            return common.response(message="同步成功")
    else:
        return common.response_method_error()


def see_api(request):
    """
    查看Api
    """
    if request.method == "POST":
        mid = request.POST.get("mid", "")
        data = MockData.objects.get(id=mid)
        api = {
            "env": data.env,
            "method": data.method,
            "uri": data.uri,
            "header": data.header,
            "request_type": data.request_type,
            "request": data.request,
            "response": data.response,
        }
        return common.response(message="获取成功！", data=api)
    else:
        return common.response_method_error()


def get_api_data(request):
    """
    获取Api数据
    """
    if request.method == "POST":
        env = request.POST.get("env", "")
        method = request.POST.get("method", "")
        uri = request.POST.get("uri", "")
        header = request.POST.get("header", "")
        request_type = request.POST.get("request_type", "")
        request_value = request.POST.get("request", "")

        if request_value != "":
            request_dict = json.loads(request_value)
        else:
            request_dict = {}

        if header != "":
            header_dict = json.loads(header)
        else:
            header_dict = {}

        if uri[0:1] == "/":
            uri = uri[1:]

        url = "http://{env}.klook.io/{uri}".format(env=env, uri=uri)
        logger.info('url:{path} method:{method} URL:{url}'.format(path=request.path, method=request.method, url=url))

        if method == "get":
            try:
                r = requests.get(url, headers=header_dict)
            except requests.exceptions.ConnectionError:
                return common.response(10102, "请检查环境！")
        elif method == "post":
            if request_type == "json":
                try:
                    r = requests.post(url, json=request_dict, headers=header_dict)
                except requests.exceptions.ConnectionError:
                    return common.response(10102, "请检查环境！")
            elif request_type == "data":
                try:
                    r = requests.post(url, data=request_dict, headers=header_dict)
                except requests.exceptions.ConnectionError:
                    return common.response(10102, "请检查环境！")
            else:
                r = requests.post(url)
        else:
            r = {}

        if r.status_code != 200:
            return common.response(10103, "接口返回状态码错误！")

        return common.response(message="获取成功！", data=r.json())
    else:
        return common.response_method_error()


def save_api_data(request):
    """
    保存Api数据
    """
    if request.method == "POST":
        env = request.POST.get("env", "")
        method = request.POST.get("method", "")
        uri = request.POST.get("uri", "")
        header = request.POST.get("header", "")
        request_type = request.POST.get("request_type", "")
        request_ = request.POST.get("request", "")
        response_ = request.POST.get("response", "")

        data = MockData.objects.all()
        uris = []
        for d in data:
            uris.append(d.uri)

        if uri not in uris:
            MockData.objects.create(uri=uri, env=env, method=method, header=header,
                                    request_type=request_type, request=request_, response=response_)

            return common.response(10200, "保存成功！")
        else:
            data = MockData.objects.get(uri=uri)
            data.env = env
            data.method = method
            data.header = header
            data.request_type = request_type
            data.request = request_
            data.response = response_
            data.save()
            return common.response(10200, "更新成功！")
    else:
        return common.response_method_error()


def mock_api(request, uri):
    """
    mock 接口，获取或更新
    """
    if request.method == "PUT":

        body = str(request.body, encoding="utf-8")
        put = QueryDict(body)
        response = put.get('response')

        data = MockData.objects.all()
        for d in data:
            if "?" in d.uri:
                if uri == d.uri.split('?')[0]:
                    d.response = response
                    d.save()
                    break
            else:
                if uri == d.uri:
                    d.response = response
                    d.save()
                    break
        else:
            return common.response(10100, "API none")

        return common.response(message="API update success!")
    else:
        data = MockData.objects.all()
        for d in data:
            if "?" in d.uri:
                if uri == d.uri.split('?')[0]:
                    response_dict = json.loads(d.response)
                    return JsonResponse(response_dict)
            else:
                if uri == d.uri:
                    response_dict = json.loads(d.response)
                    return JsonResponse(response_dict)

        else:
            return common.response(10100, "API none")


def get_help(request):
    """
    获取mock server使用帮助
    :param request:
    :return:
    """
    if request.method == "GET":
        help_file = settings.BASE_DIR + "/app_mock/docs/help.md"
        with(open(help_file, "r")) as f:
            md = f.read()
            return common.response(data=md)
    else:
        return common.response(10100, "请求方法错误")
