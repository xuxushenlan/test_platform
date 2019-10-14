from django.urls import path
from app_performance import views


urlpatterns = [
    # 性能测试数据管理
    path('', views.performance),
    path('get_data/', views.get_data),
    path('del_data/<int:data_id>/', views.delete_data),

]
