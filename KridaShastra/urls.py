"""
URL configuration for KridaShastra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home Page
    path('', views.index, name='index'),
    
    # About Page
    path('school/', views.school, name='school'),
    
    # Services Page
    path('services/', views.services, name='services'),
    
    # Networking Page
    path('products/', views.products, name='products'),
    
    # Insights Page
    path('partnership/', views.partnership, name='partnership'),
    
    # Resources Page
    path('resources/', views.resources, name='resources'),
    
    path('request-info/', views.request_info, name='request_info'),

    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
    
    # Contact Page
    path('contact/', views.contact, name='contact'),
]
