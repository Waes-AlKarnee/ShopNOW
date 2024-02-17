from django.db import models

# Create your models here.

class shopCard(models.Model):
    title = models.CharField(max_length=150)
    describtion = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    card_image = models.ImageField(upload_to="shop_image")
