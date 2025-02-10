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
from .views import HomePageView, AboutPageView
from .views import LoginViewPage, RegisterUserViewPage, LogoutViewPage
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from .views import SongListView, SongCreateView, SongUpdateView, SongDeleteView
from .views import ConcertListView, ConcertCreateView, ConcertUpdateView, ConcertDeleteView
from .views import ProductCreateView, ProductUpdateView, ProductListView, product_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),

    path('register', RegisterUserViewPage.as_view(), name='register'),
    path('login', LoginViewPage.as_view(), name='login'),
    path('logout', LogoutViewPage.as_view(), name='logout'),

    # CRUD de Álbumes
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('albums/crear', AlbumCreateView.as_view(), name='crear/album'),
    path('albums/editar/<int:pk>', AlbumUpdateView.as_view(), name='editar/album'),
    path('albums/eliminar/<int:pk>', AlbumDeleteView.as_view(), name='eliminar/album'),
    
    # CRUD de Canciones
    path('songs/', SongListView.as_view(), name='songs'),
    path('songs/crear', SongCreateView.as_view(), name='crear/song'),
    path('songs/editar/<int:pk>', SongUpdateView.as_view(), name='editar/song'),
    path('songs/eliminar/<int:pk>', SongDeleteView.as_view(), name='eliminar/song'),

     # CRUD de Conciertos
    path('concerts/', ConcertListView.as_view(), name='concerts'),
    path('concerts/crear', ConcertCreateView.as_view(), name='crear/concert'),
    path('concerts/editar/<int:pk>', ConcertUpdateView.as_view(), name='editar/concert'),
    path('concerts/eliminar/<int:pk>', ConcertDeleteView.as_view(), name='eliminar/concert'),
]