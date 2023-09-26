from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Currency)

# Register your models here.
