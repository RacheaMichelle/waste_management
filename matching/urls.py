from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [ path('', views.matches, name='matches'), 
                path('notifications/', views.notifications, name='notifications'), 
                path('notifications/mark/int:notification_id/', views.mark_notification_read, name='mark_notification_read'), 
                path('notifications/delete/int:notification_id/', views.delete_notification, name='delete_notification'), 
                path('notifications/clear/', views.clear_all_notifications, name='clear_all_notifications'), 
              ] += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

