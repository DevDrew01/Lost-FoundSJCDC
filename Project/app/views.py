from django.shortcuts import render


def home_screen(request):
    return render(request, 'app/homepage.html')

def lost_view_screen(request):
    return render(request, 'app/lostviewpage.html')

def lost_report_screen(request):
    return render(request, 'app/lostreportpage.html')

def found_view_screen(request):
    return render(request, 'app/foundviewpage.html')

def found_report_screen(request):
    return render(request, 'app/foundreportpage.html')

def login_screen(request):
    return render(request, 'app/loginpage.html')
