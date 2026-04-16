from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50, default='general')
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    def __str__(self):
        return self.name
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)