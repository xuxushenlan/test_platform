from django import forms
from django.forms import ModelForm
from interface_app.models import TestCase


# 用例表单
class TestCaseForm(ModelForm):

    class Meta:
        model = TestCase
        # 在Form中不显示的字段
        exclude = ['create_time']
