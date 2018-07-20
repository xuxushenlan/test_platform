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
    :param request: 
    :return: 
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
                    token.delete()
                except Token.DoesNotExist:
                    pass
                token = Token.objects.create(user=user)
                return common.response_succeed(message="登录成功", data={"Token":str(token)})
            else:
                return common.response_failed(message="用户名或密码错误")
    else:
        return common.response_failed(message="请求方法错误")


#@api_view(['POST'])
#@permission_classes((IsAuthenticated, ))
def get_username(request):
    """
    获取登录用户名
    """
    print(request.user, request.user.id)
    username = str(request.user)
    return common.response_succeed(data={"username":username})
