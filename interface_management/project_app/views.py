from django.shortcuts import render
from interface_management import common


# Create your views here.
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == "POST":
        pass
    else:
        common.response_failed(message="请求方法错误")
