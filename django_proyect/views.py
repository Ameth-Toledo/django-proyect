from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models.user import Usuario
from .models.album import Album
from .models.product import Product
from django.shortcuts import redirect, render, get_object_or_404
from django_proyect.view.formProduct import FormProduct
from django.contrib.auth import login, authenticate, logout
from django_proyect.view.formRegister import UserRegisterForm
from django_proyect.view.formLogin import AuthenticationForm

def index(request):
    return HttpResponse("Hola mundo")

class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Usuario
    
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
    
class ProductCreateViewPage(LoginRequiredMixin, TemplateView):  
    template_name = "products_form.html"

    def get(self, request, *args, **kwargs):
        form = FormProduct()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("Usuario no autenticado")
            return redirect("login")  

        form = FormProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.album = Album.objects.first()
            product.user = request.user  

            print(f"Usuario autenticado: {request.user}")
            product.save()
            return redirect("products")  
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
        
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
