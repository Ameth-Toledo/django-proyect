from django.db import models
from django_proyect.models.album import Album  

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duración en segundos")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.album.title}"
