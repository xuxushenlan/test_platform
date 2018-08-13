from django.shortcuts import render
from interface_management import common
from project_app.daos.project_dao import ProjectDao


# Create your views here.
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == "POST":
        req = common.json_to_dict(request.body)
        name = common.get_request_key(req, "name")
        describe = common.get_request_key(req, "describe")
        status = common.get_request_key(req, "status")

        if name is None or describe is None:
            return common.response_failed(message="必传参数为空")

        if status is None:
            status = 1

        req = ProjectDao.create_project(name, describe, status)
        if req is None:
            return common.response_failed(message="创建用例失败")

        return common.response_succeed(message="创建成功")
    else:
        return common.response_failed(message="请求方法错误")
