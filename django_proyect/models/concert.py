from django.db import models
from django_proyect.models.user import User  # Importa el modelo User

class Concert(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=150)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country} - {self.date}"
