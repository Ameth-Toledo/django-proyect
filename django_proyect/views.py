from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models.user import User
from .models.album import Album
from .models.product import Product
from django_proyect.vistas.formUser import FormUser
from django.shortcuts import redirect, render, get_object_or_404
from django_proyect.vistas.formProduct import FormProduct

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