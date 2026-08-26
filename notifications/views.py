from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Notification


@login_required
def notifications(request):
    notifications_list = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')

    Notification.objects.filter(
        recipient=request.user,
        is_read=False
    ).update(is_read=True)

    return render(request, 'notifications/notifications.html', {
        'notifications': notifications_list,
    })