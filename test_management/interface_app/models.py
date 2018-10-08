from django.db import models
from project_app.models import Project, Module


class TestCase(models.Model):
    """
    用例表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    status = models.IntegerField("状态：", default=True) # 1 可用、0 跳过
    url = models.CharField("URL", max_length=100, blank=False, default="")
    method = models.CharField("方法", max_length=100, blank=False, default="")
    header = models.CharField("Header", max_length=100, blank=True, default="")
    parameter_type = models.CharField("参数类型", max_length=10, blank=True, default="")
    parameter_body = models.TextField("参数体", max_length=1000, blank=True, default="")
    response_assert = models.CharField("返回值断言", max_length=1000, blank=True, default="")
    user = models.CharField("用户", max_length=50, blank=True, default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name
