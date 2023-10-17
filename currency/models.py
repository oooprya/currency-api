from django.db import models
from django.utils import timezone




class Currency(models.Model):
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

class Exchanger(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
    )
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255, default='Одесса')
    address = models.CharField(max_length=255)
    exchanger_info = models.CharField(max_length=255, blank=True)

    working_hours = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Обменик"
        verbose_name_plural = "Все Обменики"

class CartItem(models.Model):

    cart = models.ForeignKey(Exchanger, on_delete=models.CASCADE)
    item = models.ForeignKey(Currency, on_delete=models.CASCADE)

    buy = models.DecimalField("Покупка", decimal_places=2, max_digits=10, blank=True)
    sell = models.DecimalField("Продажа", decimal_places=2, max_digits=10, blank=True)
    sum = models.CharField("Сумма от 100 до 10000", max_length=255, blank=True)

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    def __str__(self) -> str:
        return self.item.name