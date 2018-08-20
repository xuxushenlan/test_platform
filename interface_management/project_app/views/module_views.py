from interface_management import common
from project_app.daos.project_dao import ProjectDao
from project_app.daos.module_dao import ModuleDao


def add_module(request):
    """
    添加模块
    :param request:
    :return:
    """
    if request.method == "POST":
        req = common.json_to_dict(request.body)
        project = common.get_request_key(req, "porject")
        name = common.get_request_key(req, "name")
        describe = common.get_request_key(req, "describe")

        if project is None or name is None or describe is None:
            return common.response_failed("必传参数为空")

        req = ProjectDao.get_object_by_name(name)
        if req is None:
            return common.response_failed("项目查询错误")
        
        if len(req) != 0:
            req = ModuleDao.create(req[0], name, describe)
            if req is None:
                return common.response_failed("创建模块失败")

        return common.response_succeed("创建成功")
    else:
        return common.response_failed("请求方法错误")


def update_module(request):
    """
    更新模块
    :param request:
    :return:
    """
    if request.method == "POST":
        req = common.json_to_dict(request.body)
        id_ = common.get_request_key(req, "id")
        project = common.get_request_key(req, "project")
        name = common.get_request_key(req, "name")
        describe = common.get_request_key(req, "describe")

        if id_ is None or project is None or name is None or describe is None:
            return common.response_failed("必传参数为空")

        req = ModuleDao.update(id_, project, name, describe)
        if req is None:
            return common.response_failed("更新项目失败")

        return common.response_succeed("更新成功")
    else:
        common.response_failed("请求方法错误")


def get_modules(request):
    """
    获得模块列表
    :param request:
    :return:
    """
    pass


def delete_module(request):
    """
    删除模块
    :param request:
    :return:
    """
    pass
