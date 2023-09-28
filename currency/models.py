from django.db import models
from django.utils import timezone




class Currencys(models.Model):
    name = models.CharField('Валюта', max_length=20, default='usd', unique = True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

class Currency(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    exchanger_info = models.CharField(max_length=255, blank=True)
    buy_usd = models.FloatField(null=True, blank=True, default=None)
    sell_usd = models.FloatField(null=True, blank=True, default=None)
    buy_eur = models.FloatField(null=True, blank=True, default=None)
    sell_eur = models.FloatField(null=True, blank=True, default=None)
    working_hours = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Обменик"
        verbose_name_plural = "Все Обменики"