from django.contrib import admin
from .models import Item , FavoriteItem

# Register your models here.
admin.site.register(Item)
admin.site.register(FavoriteItem)