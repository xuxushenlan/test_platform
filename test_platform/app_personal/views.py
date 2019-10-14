from django.shortcuts import render


def index(request):
    """
    登录首页
    :param request:
    :return:
    """
    return render(request, "index.html")


def login(request):
    """
    登录首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        pass
    else:
        return render(request, "login.html")
