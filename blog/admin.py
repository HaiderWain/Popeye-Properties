from django.contrib import admin
from .models import Properties
from .models import FavoriteProperties

admin.site.register(Properties)
admin.site.register(FavoriteProperties)
