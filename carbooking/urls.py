"""
URL configuration for carbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from carbooking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage),
    path('about/',views.Aboutpage),
    path('blog/',views.Blogpage),
    path('service/',views.Servicepage),
    path('contact/',views.Contactpage),
    path('feature/',views.Featurepage),
    path('cars/',views.Carspage), 
    path('team/',views.Teampage), 
    path('testimonial/',views.Testimonialpage), 
    path('page404/',views.page404page)                                                                                                                                                                                                                                                                                                                                                                 
]
