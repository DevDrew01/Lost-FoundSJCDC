from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import ItemReport
from datetime import timedelta


class Command(BaseCommand):
    help = 'Deletes items older than 7 days'

    def handle(self, *args, **kwargs):
        threshold = timezone.now() - timedelta(days=7)

        old_items = ItemReport.objects.filter(created_at__lt=threshold)
        count = old_items.count()

        old_items.delete()

        self.stdout.write(self.style.SUCCESS(f"Cleanup Successful: Deleted {count} items."))