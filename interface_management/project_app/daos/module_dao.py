"""
__author__ : 虫师
__date__: 2018.8.20
"""
import traceback
from project_app.models.module_models import Module
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from project_app.daos.project_dao import ProjectDao


class ModuleDao(object):

    @classmethod
    def get_object_by_id(cls, id_):
        """
        通过id获取数据对象
        :param id_:
        :return:
        """
        try:
            pro = Module.objects.get(id=id_)
            return pro
        except ObjectDoesNotExist:
            return None

    @classmethod
    def create(cls, porject, name, describe):
        """
        创建模块
        :param porject:
        :param name:
        :param describe:
        :return:
        """
        try:
            pro = Module.objects.create(project=project, name=name, describe=describe)
            return pro
        except Exception:
            traceback.print_exc()
            return None

    @classmethod
    def update(cls, id_, project, name, describe):
        """
        更新模块
        :param id_:
        :param project:
        :param name:
        :param describe:
        :return:
        """
        try:
            pro_obj = ProjectDao.get_object_by_name(project)
            if pro_obj is None:
                return None

            module_obj = cls.get_object_by_id(id_)
            if module_obj is None:
                return None

            module_obj.name = name
            module_obj.describe = describe
            module_obj.porject = pro_obj
            module_obj.save()
            return True
        except Exception:
            traceback.print_exc()
            return None

    @classmethod
    def get_object_by_name(cls, name):
        """
        通过name获取数据对象
        :param name:
        :return:
        """
        try:
            module = Module.objects.filter(name=name)
            return module
        except Exception:
            traceback.print_exc()
            return None

    @classmethod
    def get_list(cls):
        """
        获取模块列表
        :return:
        """
        try:
            pro_objects = Module.objects.all()
            pro_list = []
            for pro_object in pro_objects:
                pro = model_to_dict(pro_object)
                pro_list.append(pro)
            return pro_list
        except ObjectDoesNotExist:
            return None

    @classmethod
    def delete_by_id(cls, id_):
        """
        通过id删除模块
        :param id_:
        :return:
        """
        try:
            pro_obj = cls.get_object_by_id(id_)
            if pro_obj is None:
                return None

            pro_obj.delete()
            return pro_obj
        except Exception:
            traceback.print_exc()
            return None
