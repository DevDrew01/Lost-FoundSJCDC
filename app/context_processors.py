# app/context_processors.py
from .models import Notification

def notification_context(request):
    if request.user.is_authenticated:
        # Get only unread notifications for the logged-in user
        notes = Notification.objects.filter(recipient=request.user, is_read=False).order_with_respect_to('created_at')
        return {'notifications': notes}
    return {'notifications': []}