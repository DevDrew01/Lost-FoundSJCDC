from django.db import models
from django.contrib.auth.models import User

class ItemReport(models.Model):
    # This creates the dropdown options for Lost/Found
    REPORT_TYPES = [
        ('LOST', 'Lost'),
        ('FOUND', 'Found'),
    ]

    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_reported = models.DateField()
    report_type = models.CharField(max_length=5, choices=REPORT_TYPES)

    # This stores the image path (requires 'Pillow' library)
    image = models.ImageField(upload_to='item_photos/', null=True, blank=True)

    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # This links the report to a specific student (User)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.report_type}: {self.item_name}"