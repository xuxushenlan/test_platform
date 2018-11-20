from django.urls import path
from .views import testcase_views, testcase_api, testtask_views


app_name = 'interface'
urlpatterns = [
    # ex: /interface/  
    # 用例管理  
    path("testcase/", testcase_views.testcase),
    path("add_case/", testcase_views.add_case),
    path("debug_case/<int:cid>/", testcase_views.debug_case),
    path("debug/", testcase_views.api_debug),
    path("get_case_info/", testcase_views.get_case_info),
    path("get_project_list", testcase_api.get_project_list),
    
    # 任务管理
    path("testtask/", testtask_views.testtask),
    path("add_task/", testtask_views.add_task),
    path("add_test_cases/", testtask_views.add_test_cases),

]
