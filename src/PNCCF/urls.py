"""PNCCF URL Configuration

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
from django.urls import path
from formular.views import HomeView
from django.views.generic import TemplateView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'formular1/', TemplateView.as_view(template_name ='formular1.html')),
    path(r'formular2/', TemplateView.as_view(template_name ="formular2.html")),
    path(r'instructiuni/', TemplateView.as_view(template_name="instructiuni.html")),
    path(r'', HomeView.as_view()),
    path(r'contact/', TemplateView.as_view(template_name="contact.html")),
]
