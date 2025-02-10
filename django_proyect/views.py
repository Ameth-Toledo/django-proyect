from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView, DeleteView
from .models.user import User
from .models.album import Album
from .models.product import Product
from .models.song import Song
from django_proyect.vistas.formUser import FormUser
from django.shortcuts import redirect, render, get_object_or_404
from django_proyect.vistas.formProduct import FormProduct
from django_proyect.vistas.formAlbum import AlbumForm
from django.urls import reverse_lazy
from django_proyect.vistas.formSong import SongForm

def index(request):
    return HttpResponse("Hola mundo")

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = User
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Usuarios recientes"
        context["Lista"] = self.model.objects.all()
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ProductsPageView(TemplateView):
    template_name = 'products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Productos disponibles"
        context["products"] = Product.objects.all()
        return context
    
class ProductCreateViewPage(TemplateView):
    template_name = "products_form.html"

    def get(self, request, *args, **kwargs):
        form = FormProduct()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.album = Album.objects.first() 
            product.user = User.objects.first()    
            product.save()
            return redirect("products") 
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

# CRUD de Álbumes
class AlbumListView(ListView):
    model = Album
    template_name = 'albums.html'
    context_object_name = 'albums'

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums_form.html'
    success_url = reverse_lazy('albums')

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums_form.html'
    success_url = reverse_lazy('albums')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums_confirm_delete.html'
    success_url = reverse_lazy('albums')

# CRUD de Canciones
class SongListView(ListView):
    model = Song
    template_name = 'songs.html'
    context_object_name = 'songs'

class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'songs_form.html'
    success_url = reverse_lazy('songs')

    def form_valid(self, form):
        album = form.cleaned_data.get('album')
        if not Album.objects.filter(id=album.id).exists():
            form.add_error('album', 'El álbum seleccionado no existe.')
            return self.form_invalid(form)
        return super().form_valid(form)

class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'songs_form.html'
    success_url = reverse_lazy('songs')

class SongDeleteView(DeleteView):
    model = Song
    template_name = 'songs_confirm_delete.html'
    success_url = reverse_lazy('songs')
