from django.contrib import admin
from .models import Exchanger, Currency, CartItem

class CurrencyInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "exchanger", "exchanger_id", "currency", 'buy', 'sell', 'sum')
    list_editable = ('buy', 'sell', 'sum')
    list_display_links = ["exchanger"]

class ExchangerAdmin(admin.ModelAdmin):
    inlines = [CurrencyInline]
    list_display = ["id","address"]
    list_display_links = ["address"]


admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Currency)
admin.site.register(Exchanger, ExchangerAdmin)

# Register your models here.
