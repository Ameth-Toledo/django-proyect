from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    genre = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
