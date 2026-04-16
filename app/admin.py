from django.contrib import admin
from .models import ItemReport


@admin.register(ItemReport)
class ItemReportAdmin(admin.ModelAdmin):
    # This determines what columns you see in the admin list view
    list_display = ('item_name', 'report_type', 'location', 'date_reported', 'created_at')

    # Adds a sidebar to filter by type or location
    list_filter = ('report_type', 'location', 'category')

    # Adds a search bar specifically for the admin panel
    search_fields = ('item_name', 'description', 'contact_info')

    # Allows you to click the date to sort
    date_hierarchy = 'created_at'
