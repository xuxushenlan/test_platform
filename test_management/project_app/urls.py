from django.urls import path
from .views import project_views, module_views


app_name = 'manage'
urlpatterns = [
    # ex: /manage/  
    # 项目管理
    path('', project_views.project_manage),    
    path('project/', project_views.project_manage),
    path('add_project/', project_views.add_project),
    path("edit_project/<int:pid>/", project_views.edit_project),
    path("delete_project/<int:pid>/", project_views.delete_project),
    
    # 模块管理
    path('module/', module_views.module_manage),
    path('add_module/', module_views.add_module),
    path('edit_module/<int:mid>/', module_views.edit_module),
    path('delete_module/<int:mid>/',module_views.delete_module),
]
