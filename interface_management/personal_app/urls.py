from django.urls import path
from personal_app.views import user_views

urlpatterns = [
    path('login', user_views.user_login),
]
