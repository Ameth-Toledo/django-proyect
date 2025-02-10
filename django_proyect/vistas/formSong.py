from django import forms
from ..models.song import Song
from ..models.album import Album

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album']

    def clean_album(self):
        album = self.cleaned_data.get('album')
        if not album:
            raise forms.ValidationError("Debe seleccionar un álbum existente.")
        return album
