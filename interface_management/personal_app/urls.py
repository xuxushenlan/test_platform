from django.urls import path
from rest_framework.authtoken import views
from personal_app.views import user_views


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('user_login', user_views.user_login),
]
