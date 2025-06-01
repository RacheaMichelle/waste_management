from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Matches page (for listing matched waste notifications)
    path('', views.matches, name='matches'),

    # Notifications list page
    path('notifications/', views.notifications, name='notifications'),

    # Mark a single notification as read
    path('notifications/mark/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),

    # Delete a single notification
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),

    # Clear (delete) all notifications
    path('notifications/clear/', views.clear_all_notifications, name='clear_all_notifications'),
]

# Add static media serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
