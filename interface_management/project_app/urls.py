from django.urls import path
from project_app import views


urlpatterns = [
    path('add_project', views.add_project),
]
