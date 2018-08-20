"""
__author__ : 虫师
__date__: 2018.8.16
"""
import traceback
from project_app.models.module_models import Module
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


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
    def update(cls, id_, name, describe, status):
        """
        更新模块
        :param id_:
        :param name:
        :param describe:
        :param status:
        :return:
        """
        try:
            pro_obj = cls.get_object_by_id(id_)
            if pro_obj is None:
                return None

            pro_obj.name = name
            pro_obj.describe = describe
            pro_obj.status = status
            pro_obj.save()
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
            pro = Module.objects.filter(name=name)
            return pro
        except Exception:
            traceback.print_exc()
            return None

    @classmethod
    def get_object_list(cls):
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
