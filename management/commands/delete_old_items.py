from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import ItemReport  # Make sure this matches your model name
from datetime import timedelta


class Command(BaseCommand):
    help = 'Deletes items older than 7 days'

    def handle(self, *args, **kwargs):
        threshold_date = timezone.now() - timedelta(days=7)
        old_items = ItemReport.objects.filter(date_reported__lt=threshold_date)
        count = old_items.count()
        old_items.delete()

        self.stdout.write(f"Successfully deleted {count} items older than 7 days.")