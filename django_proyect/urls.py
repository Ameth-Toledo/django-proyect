from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, AboutPageView, ProductsPageView
from .views import ProductCreateViewPage
from .views import LoginViewPage, RegisterUserViewPage, LogoutViewPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductsPageView.as_view(), name='products'),
    path('products/crear', ProductCreateViewPage.as_view(), name='crear/producto'),
]
