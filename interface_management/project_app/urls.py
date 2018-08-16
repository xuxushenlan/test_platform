from django.urls import path
from project_app.views import project_views


urlpatterns = [

    # 项目管理
    path('add_project', project_views.add_project),
    path('update_project', project_views.update_project),
    path('get_projects', project_views.get_projects),
    path('del_project', project_views.delete_project),
]
