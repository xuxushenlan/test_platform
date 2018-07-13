from django.urls import path
from personal_app.views import user_views


urlpatterns = [
    path('user_login', user_views.user_login),
    path('user_auth_test', user_views.user_auth_test),
]
