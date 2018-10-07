from django.urls import path
from .views import testcase_views


app_name = 'interface'
urlpatterns = [
    # ex: /interface/  
    # 用例管理  
    path("testcase/", testcase_views.testcase),
    path("add_case/", testcase_views.add_case),
    path("debug_case/<int:cid>/", testcase_views.debug_case)
]