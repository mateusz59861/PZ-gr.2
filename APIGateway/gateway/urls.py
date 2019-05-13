"""APIGateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path('v1/metrics', views.metrics, name='results'),
    path('v1/metrics/<str:metrics_id>', views.metrics, name='results'),
    path('v1/metrics/<str:metrics_id>/measurements', views.metrics_measurements, name='results'),
    path('v1/hosts', views.hosts, name='results'),
    path('v1/hosts/<str:hosts_id>', views.hosts, name='results'),
    path('v1/monitors', views.monitors, name='results'),
]