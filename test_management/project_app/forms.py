from django import forms
from django.forms import ModelForm
from project_app.models import Project, Module
from django.forms import fields


# Form项目表单
class AddProjectForm(forms.Form):
    name = forms.CharField(max_length=100)            # 名称
    describe = forms.CharField(max_length=300)        # 描述


# modelForm 项目表单
class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        # 在Form中显示的字段
        # fields = ['name']
        # 在Form中不显示的字段
        exclude = ['create_time']

        # 定义表单属性
        # widgets = {
        #     'name': forms.SelectMultiple(attrs={'class': 'input-small'}),
        # }


class ModuleForm(ModelForm):
    
    class Meta:
        model = Module
        # 在Form中不显示的字段
        exclude = ['create_time']
