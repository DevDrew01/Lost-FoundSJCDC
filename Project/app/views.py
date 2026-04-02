from django.shortcuts import render
from django.views.generic import TemplateView

class LogInPageView(TemplateView):
    template_name = 'app/LogInPage.html'

# Create your views here.
