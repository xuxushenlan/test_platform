from django import forms
from django.forms import ModelForm
from project_app.models import Project, Module
from django.forms import fields


# 添加项目表单
class AddProjectForm(forms.Form):
    name = forms.CharField(max_length=100)            # 名称
    describe = forms.CharField(max_length=300)        # 描述


# 添加模块表单
class AddModuleForm(forms.Form):
    project = fields.ChoiceField(
        choices=Project.objects.values_list('id', 'name')
    )

    def __init__(self, *args, **kwargs):
        super(AddModuleForm, self).__init__(*args, **kwargs)
        self.fields['project'].choices = Project.objects.values_list('id', 'name')
