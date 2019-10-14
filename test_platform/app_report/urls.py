from django.urls import path
from app_report import views


urlpatterns = [

    # page
    path('', views.report_list),
    path('scan_report', views.scan_report),

    path('snapshot/<int:rid>/', views.snapshot_list),
    path('<int:rid>/', views.report_preview),
    path('case_tree/', views.case_tree),
    path('case_screenshots/', views.case_screenshots),
    path('test/', views.test),

]
