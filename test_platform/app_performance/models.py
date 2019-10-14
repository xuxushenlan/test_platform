from django.db import models


# Create your models here.
class TestData(models.Model):
    """
    gamebench性能测试数据列表
    """
    session_id = models.CharField("session_id", max_length=50, null=False)
    device = models.TextField("设备", default="")
    # platform = models.CharField("平台", default="")
    app = models.CharField("App", max_length=30, null=False)
    app_version = models.CharField("App版本", max_length=10, null=False)
    pushed_time = models.DateTimeField("push_time", null=False)

    cpu_usage_avg = models.FloatField("CPU平均值", null=True)
    cpu_usage_median = models.FloatField("CPU中间值", null=True)
    cpu_usage_min = models.FloatField("CPU最小值", null=True)
    cpu_usage_max = models.FloatField("CPU最大值", null=True)

    mem_usage_avg = models.IntegerField("Memory平均使用率", null=True)
    mem_usage_median = models.IntegerField("Memory中间值", null=True)
    mem_usage_min = models.IntegerField("Memory最小值", null=True)
    mem_usage_max = models.IntegerField("Memory最大值", null=True)

    fps_min = models.IntegerField("FPS最小值", null=True)
    fps_max = models.IntegerField("FPS最大值", null=True)
    fps_median = models.IntegerField("FPS中间价值", null=True)
    fps_stability = models.FloatField("FPS稳定性", null=True)

    status = models.BooleanField("开关", default=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_id
