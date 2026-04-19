from .models import Notification

def notification_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).order_by('-created_at')

        return {
            'notifications': notifications,
            'unread_notifications_count': notifications.count()
        }
    return {
        'notifications': [],
        'unread_notifications_count': 0
    }