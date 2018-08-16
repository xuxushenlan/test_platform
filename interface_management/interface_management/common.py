import json
from django.http import JsonResponse
from json.decoder import JSONDecodeError


def json_to_dict(body):
    """
    把json数据转换为dict
    :param body: json格式数据
    :return: dict
    """
    try:
        re = json.loads(body)
    except JSONDecodeError:
        return {}
    else:
        return re


def get_request_key(req, key):
    """
    获取
    :param req: dict格式
    :param key: 关键字
    :return: data
    """
    re = None
    if key in req:
        re = req[key]
    return re


def response_succeed(message="请求成功", data={}):
    """
    响应成功
    :param message: 说明
    :param data: 详细数据
    :return:
    """
    content = {
        "success": "true",
        "message": message,
        "data": data,
    }
    return JsonResponse(content)


def response_failed(message="参数错误"):
    """
    响应失败
    :param message:
    :return:
    """
    content = {
        "success": "false",
        "message": message,
    }
    return JsonResponse(content)
