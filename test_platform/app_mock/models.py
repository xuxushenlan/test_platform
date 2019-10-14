from django.db import models


class MockData(models.Model):
    """
    mock数据
    """
    uri = models.CharField("uri", max_length=200, null=False)
    env = models.CharField("env", max_length=20, default="")
    method = models.CharField("方法", max_length=10, default="get")
    desc = models.TextField("描述", default="")
    header = models.TextField("请求头", default="{}")
    request_type = models.TextField("请求参数类型", default="")
    request = models.TextField("请求参数", default="{}")
    response = models.TextField("返回参数", default="")
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri

    class Meta:
        ordering = ['-id']
