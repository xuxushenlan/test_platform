from django.db import models


class TestReport(models.Model):
    """
    自动化测试报告列表
    """
    name = models.CharField("报告完整名称", max_length=200, null=False)
    data_time = models.CharField("报告日期时间", max_length=200, null=True)
    version = models.CharField("版本", max_length=100, null=True)
    platform = models.CharField("平台", max_length=100, null=True)
    error = models.IntegerField("错误用例", default=0)
    failure = models.IntegerField("失败用例", default=0)
    skipped = models.IntegerField("跳过用例", default=0)
    tests = models.IntegerField("总用例数", default=0)
    run_time = models.FloatField("运行时长", default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class TestFile(models.Model):
    """
    自动化测试文件
    """
    report = models.ForeignKey(TestReport, on_delete=models.CASCADE)
    file_name = models.CharField("测试文件名", max_length=100, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class TestCase(models.Model):
    """
    自动化测试用例
    """
    file = models.ForeignKey(TestFile, on_delete=models.CASCADE)
    case_name = models.CharField("用例名", max_length=100, null=False)
    case_desc = models.CharField("用例描述", max_length=500, null=True, default="")
    is_pass = models.BooleanField("是否通过", null=True)
    fail_desc = models.CharField("用例失败描述", max_length=200, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.case_name


class TestSnapshot(models.Model):
    """
    自动化测试用例截图
    """
    case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    step_name = models.CharField("测试步骤截图", max_length=100, null=False)
    full_path = models.CharField("完整的路径", max_length=200, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_path

    class Meta:
        ordering = ['-id']
