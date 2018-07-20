from django.urls import path
from personal_app.views import user_views
#from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('user_login', user_views.user_login),
    #path('get_username', csrf_exempt(user_views.get_username)),
    path('get_username', user_views.get_username),
]
