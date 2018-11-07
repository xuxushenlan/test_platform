from django.urls import path
from .views import testcase_views, testtask_views


app_name = 'interface'
urlpatterns = [
    # ex: /interface/  
    # 用例管理  
    path("testcase/", testcase_views.testcase),
    path("add_case/", testcase_views.add_case),
    path("debug_case/<int:cid>/", testcase_views.debug_case),
    path('debug/', testcase_views.api_debug),

    # 任务管理
    path("testtask/", testtask_views.testtask),
    path("add_test_cases/", testtask_views.add_test_cases),
]
