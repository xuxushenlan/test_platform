from django.urls import path
from project_app.views import project_views


urlpatterns = [

    # 项目管理
    path('add_project', project_views.add_project),
]
