from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_screen, name='home'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('claim/<int:item_id>/', views.claim_item, name='claim_item'),
    path('found-report/', views.found_report_screen, name='found_report'),
    path('lost-report/', views.lost_report_screen, name='lost_report'),
    path('', views.login_screen, name='login'),


]