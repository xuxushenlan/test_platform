from django.urls import path
from project_app.views import project_views
from project_app.views import module_views


urlpatterns = [

    # 项目管理
    path('add_project', project_views.add_project),
    path('get_project_info', project_views.get_project_info),
    path('update_project', project_views.update_project),
    path('get_projects', project_views.get_projects),
    path('del_project', project_views.delete_project),

    # 服务管理
    path('add_module', module_views.add_module),
    path('update_module', module_views.update_module),
    path('get_modules', module_views.get_modules),
    path('del_module', module_views.delete_module),
]
