from django.urls import path
from personal_app.views import user_views

urlpatterns = [
    path('user_login', user_views.user_login),
    path('user_logout', user_views.user_logout),
    path('get_username', user_views.get_username),
]
