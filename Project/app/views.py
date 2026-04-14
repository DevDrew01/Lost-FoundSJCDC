from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import ItemReport
from .forms import ItemReportForm


def home_screen(request):
    query = request.GET.get('q', '')
    report_type = request.GET.get('type', 'All')
    location = request.GET.get('location', 'All')

    items = ItemReport.objects.all().order_by('-created_at')

    if query:
        items = items.filter(Q(item_name__icontains=query) | Q(description__icontains=query))

    if report_type != 'All' and report_type != '':
        items = items.filter(report_type=report_type)

    if location != 'All' and location != '':
        items = items.filter(location=location)

    context = {
        'items': items,
        'query': query,
        'current_type': report_type,
        'current_location': location,
    }
    return render(request, 'app/homepage.html', context)

def item_detail(request, pk):
    # Find one specific item by its ID (pk)
    item = get_object_or_404(ItemReport, pk=pk)
    return render(request, 'app/item_detail.html', {'item': item})


def lost_report_screen(request):
    if request.method == 'POST':
        form = ItemReportForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.report_type = 'LOST'
            item.save()
            return redirect('home')
    else:
        form = ItemReportForm()

    return render(request, 'app/lostreportpage.html', {'form': form})


def found_report_screen(request):
    if request.method == 'POST':
        form = ItemReportForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.report_type = 'FOUND'
            item.save()
            return redirect('home')
    else:
        form = ItemReportForm()

    return render(request, 'app/foundreportpage.html', {'form': form})

def login_screen(request):
    return render(request, 'app/loginpage.html')
