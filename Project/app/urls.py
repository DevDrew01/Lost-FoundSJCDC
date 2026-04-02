from django.urls import path
from .views import LogInPageView

urlpatterns = [
    path('', LogInPageView.as_view(), name='login'),
]