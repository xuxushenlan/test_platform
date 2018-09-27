from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /manage/
    path('', views.project_manage),
    path('project/', views.project_manage),
    path('add_project/', views.add_project),
    # path('edit_project/<int:pk>/', views.ProjectUpdate.as_view(), name="edit"),
    path('module/', views.module_manage),
    path('add_module/', views.add_module),
    path('add_module/', views.add_module),
]
