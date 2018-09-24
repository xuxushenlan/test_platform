from django import forms
from django.forms import ModelForm
from project_app.models import Project


# 添加项目表单
class AddProjectForm(forms.Form):
    name = forms.CharField(max_length=100)            # 名称
    describe = forms.CharField(max_length=300)                      # 描述

