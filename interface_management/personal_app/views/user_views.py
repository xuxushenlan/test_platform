from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from interface_management import common
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated


def user_login(request):
    """
    用户登录
    """
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return common.response_failed(message="用户名密码为空")
        else:
            user = auth.authenticate(username=login_username, password=login_password)
            if user is not None and user.is_active:
                auth.login(request, user)  # 验证登录
                # update the token
                try:
                    token = Token.objects.get(user=user)
                except Token.DoesNotExist:
                    pass
                else:
                    token.delete()
                token = Token.objects.create(user=user)
                return common.response_succeed(message="登录成功", data={"Token":str(token)})
            else:
                return common.response_failed(message="用户名或密码错误")
    else:
        return common.response_failed(message="请求方法错误")


def get_username(request):
    """
    获取登录用户名
    """
    username = str(request.user)
    return common.response_succeed(data={"username":username})


def user_logout(request):
    """
    退出登录
    """
    token = Token.objects.get(user=request.user)
    token.delete()
    return common.response_succeed()
