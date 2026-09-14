from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drons import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mains.urls')),
    path('index.html', include('mains.urls')),
    path('about.html', include('mains.urls')),
    path('services.html', include('mains.urls')),
    path('garage.html', include('mains.urls')),
    path('blog.html', include('mains.urls')),
    path('blog_details.html', include('mains.urls')),
    path('elements.html', include('mains.urls')),
    path('contact.html', include('mains.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)