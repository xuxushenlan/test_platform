import traceback
from project_app.models.project_models import Project


class ProjectDao(object):

    @classmethod
    def create_project(cls, name, describe, status):
        """
        创建项目
        :param name:
        :param describe:
        :param status:
        :return:
        """
        try:
            pro = Project.objects.create(name=name, describe=describe, status=int(status))
            return pro
        except Exception:
            traceback.print_exc()
            return None
