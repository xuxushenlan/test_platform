from interface_management import common
from project_app.daos.project_dao import ProjectDao


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
            return common.response_failed("必传参数为空")

        if status is None:
            status = True
        elif isinstance(status, bool) is False:
            return common.response_failed("状态类型错误")

        req = ProjectDao.get_object_by_name(name)
        if req is None:
            return common.response_failed("项目查询错误")
        elif len(req) != 0:
            return common.response_failed("项目已经存在")

        req = ProjectDao.create(name, describe, status)
        if req is None:
            return common.response_failed("创建项目失败")

        return common.response_succeed("创建成功")
    else:
        return common.response_failed("请求方法错误")


def update_project(request):
    """
    更新项目
    :param request:
    :return:
    """
    if request.method == "POST":
        req = common.json_to_dict(request.body)
        id_ = common.get_request_key(req, "id")
        name = common.get_request_key(req, "name")
        describe = common.get_request_key(req, "describe")
        status = common.get_request_key(req, "status")

        if id_ is None or name is None or describe is None:
            return common.response_failed("必传参数为空")

        if status is None:
            status = True
        elif isinstance(status, bool) is False:
            return common.response_failed("状态类型错误")

        req = ProjectDao.update(id_, name, describe, status)
        if req is None:
            return common.response_failed("更新项目失败")

        return common.response_succeed("更新成功")
    else:
        common.response_failed("请求方法错误")


def get_projects(request):
    """
    获得对象列表
    :param request:
    :return:
    """
    if request.method == "GET":
        req = ProjectDao.get_object_list()
        if req is None:
            return common.response_failed("查询失败")

        return common.response_succeed("查询成功", data=req)
    else:
        return common.response_failed("请求方法错误")


def delete_project(request):
    """
    删除project
    :param request:
    :return:
    """
    if request.method == "POST":
        req = common.json_to_dict(request.body)
        id_ = common.get_request_key(req, "id")

        if id_ is None:
            return common.response_failed("id不能为空")

        ret = ProjectDao.delete_by_id(id_)
        if ret is None:
            return common.response_failed("删除失败")

        return common.response_succeed("删除成功")
    else:
        return common.response_failed("请求方法错误")
