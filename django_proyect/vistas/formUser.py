from django import forms
from ..models.user import User

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']