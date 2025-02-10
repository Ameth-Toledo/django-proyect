from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, AboutPageView, ProductsPageView
from .views import ProductCreateViewPage
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from .views import SongListView, SongCreateView, SongUpdateView, SongDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('products/crear', ProductCreateViewPage.as_view(), name='crear/producto'),
    
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
]
