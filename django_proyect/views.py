from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView, UpdateView, DeleteView
from .models.user import Usuario
from .models.album import Album
from .models.song import Song
from .models.concert import Concert
from .models.product import Product
from django.shortcuts import redirect, render, get_object_or_404
from django_proyect.view.formProduct import FormProduct
from django_proyect.view.formAlbum import AlbumForm
from django_proyect.view.formSong import SongForm
from django_proyect.view.formConcert import ConcertForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django_proyect.view.formRegister import UserRegisterForm
from django_proyect.view.formLogin import AuthenticationForm
from django.views.generic import CreateView

def index(request):
    return HttpResponse("Hola mundo")

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Usuarios recientes"
        context["Lista"] = self.model.objects.all()
        context["products"] = Product.objects.all()  # Se agregan los productos al contexto
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'

class ProductCreateView(View):
    def post(self, request, *args, **kwargs):
        form = FormProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.album = Album.objects.first() 
            product.user = Usuario.objects.first()    
            product.save()
        return redirect("products")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = FormProduct
    template_name = "products_list.html"  
    success_url = reverse_lazy("products")

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
    return redirect("products")

class RegisterUserViewPage(View):
    template_name = 'register.html'
    
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'register.html', {'form': form})
    
class LoginViewPage(View):
    template_name = 'login.html'
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Credenciales inválidas')
            return render(request, 'login.html', {'form': form})
        
class LogoutViewPage(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
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
        if album is None:
            form.add_error('album', 'Debes seleccionar un álbum.')
            return self.form_invalid(form)
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

class ConcertListView(ListView):
    model = Concert
    template_name = 'concerts.html'
    context_object_name = 'concerts'

class ConcertCreateView(CreateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'concerts_form.html'
    success_url = reverse_lazy('concerts')

class ConcertUpdateView(UpdateView):
    model = Concert
    form_class = ConcertForm
    template_name = 'concerts_form.html'
    success_url = reverse_lazy('concerts')

class ConcertDeleteView(DeleteView):
    model = Concert
    template_name = 'concerts_confirm_delete.html'
    success_url = reverse_lazy('concerts')
