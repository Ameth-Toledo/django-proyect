from django import forms
from ..models.album import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'year', 'genre', 'image']