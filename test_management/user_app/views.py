from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def index(request):
    """
    登陆首页
    :param request:
    :return:
    """
    return render(request, "index.html")


def login_action(request):
    """
    登陆动作处理
    :param request:
    :return:
    """
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return render(request, "index.html", {"error": "username or password null"})
        else:
            user = auth.authenticate(username=login_username, password=login_password)
            if user is not None:
                auth.login(request, user)   # 记录用户登录状态
                response = HttpResponseRedirect('/manage/project/')
                request.session['user'] = login_username
                return response
            else:
                return render(request, "index.html", {"error": "username or password error"})
    else:
        return render(request, "index.html")


def logout(request):
    """
    退出登录
    :param request:
    :return:
    """
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
