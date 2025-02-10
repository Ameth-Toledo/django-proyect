from django import forms
from ..models.concert import Concert

class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ['city', 'country', 'date', 'venue']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }