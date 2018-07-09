import json
from django.http import JsonResponse
from json.decoder import JSONDecodeError

def json_to_dict(body):
    """
    把json数据转换为dict
    :param body: json格式数据
    :return: dict
    """
    re = None
    try:
        re = json.loads(body)
    except JSONDecodeError as e:
        re = {}
    return re


def response_succeed(success="true", message="请求成功", data={}):
    """
    响应成功
    :param success: 结果
    :param message: 说明
    :param data: 详细数据
    :return:
    """
    content = dict()
    content["success"] = success
    content["message"] = message
    content["data"] = data
    return JsonResponse(content)


def response_failed(success="false",message="参数错误"):
    """
    响应失败
    :param message:
    :return:
    """
    content = dict()
    content["success"] = success
    content["message"] = message
    return JsonResponse(content)
