from django.contrib import admin
from .models import Category, Currency, Currencys

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'city', 'exchanger_info' ]
    list_display_links = ('address', 'city')
    list_editable = ['exchanger_info']

admin.site.register(Category)
admin.site.register(Currencys)


# Register your models here.
