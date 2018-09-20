from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /manage/
    path('', views.project_manage),
]
