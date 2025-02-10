"""
URL configuration for django_proyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import HomePageView, AboutPageView, ProductsPageView
from .views import ProductCreateViewPage
from .views import LoginViewPage, RegisterUserViewPage, LogoutViewPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('products/crear', ProductCreateViewPage.as_view(), name='crear/producto'),
    path('register', RegisterUserViewPage.as_view(), name='register'),
    path('login', LoginViewPage.as_view(), name='login'),
    path('logout', LogoutViewPage.as_view(), name='logout'),
]
