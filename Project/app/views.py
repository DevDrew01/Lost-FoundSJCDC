from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import ItemReport
from .forms import ItemReportForm


def home_screen(request):
    query = request.GET.get('q', '')
    report_type = request.GET.get('type', 'All')
    location = request.GET.get('location', 'All')

    items_list = ItemReport.objects.all().order_by('-created_at')

    if query:
        items_list = items_list.filter(
            Q(item_name__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    if report_type != 'All':
        items_list = items_list.filter(report_type=report_type)

    if location != 'All':
        items_list = items_list.filter(location=location)

    paginator = Paginator(items_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': page_obj,
        'query': query,
        'current_type': report_type,
        'current_location': location,
    }
    return render(request, 'app/homepage.html', context)

def item_detail(request, pk):
    # Find one specific item by its ID (pk)
    item = get_object_or_404(ItemReport, pk=pk)
    return render(request, 'app/itemdetail.html', {'item': item})

def lost_report_screen(request):
    if request.method == 'POST':
        save_item_report(request, 'LOST')
        return redirect('home')
    return render(request, 'app/lostreportpage.html')

def found_report_screen(request):
    if request.method == 'POST':
        save_item_report(request, 'FOUND')
        return redirect('home')
    return render(request, 'app/foundreportpage.html')

def save_item_report(request, r_type):
    item_name = request.POST.get('item_name')
    category = request.POST.get('category')
    description = request.POST.get('description')
    location = request.POST.get('location')
    date_val = request.POST.get('date_lost')
    contact = request.POST.get('contact')
    image = request.FILES.get('image')

    # Assign user only if they are authenticated, otherwise None
    report_user = request.user if request.user.is_authenticated else None

    ItemReport.objects.create(
        item_name=item_name,
        category=category,
        description=description,
        location=location,
        date_reported=date_val,
        contact_info=contact,
        report_type=r_type,
        image=image,
        user=report_user
    )


@require_POST
def claim_item(request, item_id): # Ensure 'item_id' is here
    item = get_object_or_404(ItemReport, id=item_id)
    item.report_type = 'CLAIMED'
    item.save()
    return JsonResponse({'status': 'success'})

def login_screen(request):
    return render(request, 'app/loginpage.html')
