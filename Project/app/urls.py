from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('found-report/', views.found_report_screen, name='found_report'),
    path('lost-report/', views.lost_report_screen, name='lost_report'),
    path('', views.login_screen, name='login'),


]