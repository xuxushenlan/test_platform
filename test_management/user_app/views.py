from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# 登陆
def index(request):
    return render(request, "index.html")


# 登录处理
def login_action(request):
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")
        if login_username == '' or login_password == '':
            return render(request,"index.html", {"error":"username or password null"})
        else:
            user = auth.authenticate(username = login_username, password = login_password)
            if user is not None:
                auth.login(request, user) # 验证登录
                response = HttpResponseRedirect('/manage/project/')
                # response.set_cookie('user',login_username, 3600)
                request.session['user'] = login_username # 将 session 信息记录到浏览器
                print("login???")
                return response
            else:
                return render(request,"index.html", {"error":"username or password error"})
    else:
        return render(request, "index.html")
