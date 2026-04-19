from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

# This line is the "magic" that connects the URL to the actual folder
if settings.DEBUG or not settings.DEBUG: # Force it to work in production too
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)