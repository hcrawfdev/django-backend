"""renovatrBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    path('accounts/api/',include('accounts.urls')),
    path('posts/', include('post.urls'), name='posts'),
    path('admin/', admin.site.urls),
]


# "email": "faker@faker.com",
   # "username": "TestBoy",
   # "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IlRlc3RCb3kiLCJleHAiOjE1MzEzNDg0OTQsImVtYWlsIjoiZmFrZXJAZmFrZXIuY29tIn0.ugM3CXu5Vrq61VU1NjPh1PTCMF_8JHLfmV3qINz88n8"