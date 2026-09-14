from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('about.html', views.about),
    path('services.html', views.services),
    path('garage.html', views.projects),
    path('blog.html', views.blog),
    path('blog_details.html', views.blog_details),
    path('elements.html', views.elements),
    path('contact.html', views.contacts),
]