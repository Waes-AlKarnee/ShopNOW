from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(shopCard)

class shopCardAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'describtion', 'date_posted', 'card_image']
