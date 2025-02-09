from django.db import models
from django_proyect.models.album import Album

class Song(models.Model):
    title = models.CharField(max_length=150)
    duration = models.DurationField()  
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
