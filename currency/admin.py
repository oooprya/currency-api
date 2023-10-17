from django.contrib import admin
from .models import Exchanger, Currency, CartItem


class CurrencyInline(admin.TabularInline):
    model = CartItem
    extra = 1

class ExchangerAdmin(admin.ModelAdmin):
    inlines = [CurrencyInline]
    list_display = ["id","address"]
    list_display_links = ["address"]


admin.site.register(Currency)
admin.site.register(Exchanger, ExchangerAdmin)

# Register your models here.
