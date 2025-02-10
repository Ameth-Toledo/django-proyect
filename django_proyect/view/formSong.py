from django import forms
from django_proyect.models.song import Song
from django_proyect.models.album import Album

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album']  

    def clean_album(self):
        album = self.cleaned_data.get('album')
        if album is None:
            raise forms.ValidationError('Debes seleccionar un álbum.')
        if not Album.objects.filter(id=album.id).exists():
            raise forms.ValidationError('El álbum seleccionado no existe.')
        return album
