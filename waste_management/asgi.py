# waste_management/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waste_management.settings')

# For Vercel, use HTTP only - disable WebSockets if they cause issues
application = get_asgi_application()
