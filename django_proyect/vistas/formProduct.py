from django import forms
from ..models.product import Product

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image', 'album', 'user']