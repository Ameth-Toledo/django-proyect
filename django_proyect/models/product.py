from django.db import models
from django_proyect.models.user import User
from django_proyect.models.album import Album

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.CharField(max_length=255, null=True, blank=True)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
