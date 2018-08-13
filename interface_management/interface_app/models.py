from django.db import models
from project_app.models import Module


# Create your models here.
class Module(models.Model):
    """
    用例表
    """
    Project = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name
