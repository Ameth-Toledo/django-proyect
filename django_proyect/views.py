from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models.user import User
from django_proyect.vistas.formUser import FormUser
from django.shortcuts import redirect, render, get_object_or_404

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