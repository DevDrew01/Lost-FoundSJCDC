from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home'),
    path('', views.found_view_screen, name='found_view'),
    path('found-report/', views.found_report_screen, name='found_report'),
    path('', views.lost_view_screen, name='lost_view'),
    path('lost-report/', views.lost_report_screen, name='lost_report'),
    path('', views.login_screen, name='login'),

]