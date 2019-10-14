"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView
from app_personal.views import index, login
from app_mock.views import view_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='static/image/favicon.png')),

    # 首页
    path('', index),
    path('login', login),

    # 性能测试结果管理
    path('performance/', include('app_performance.urls')),

    # mock api管理
    path('mock/', include('app_mock.urls')),
    re_path('^api/(?P<uri>\S+)', view_api.mock_api),

    # 自动化测试报告管理
    path('report/', include('app_report.urls')),
]
