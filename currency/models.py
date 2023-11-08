from django.db import models
from django.utils import timezone




class Currency(models.Model):
    name = models.CharField('Валюта', max_length=20, default='usd', unique = True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Exchanger(models.Model):
    address = models.CharField(max_length=255)

    exchanger_info = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length = 16, help_text='+38096-123-45-67')
    working_hours = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Обменик"
        verbose_name_plural = "Все Обменики"

class CartItem(models.Model):

    exchanger = models.ForeignKey(Exchanger, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    buy = models.DecimalField("Покупка", decimal_places=2, max_digits=10, blank=True)
    sell = models.DecimalField("Продажа", decimal_places=2, max_digits=10, blank=True)
    sum = models.CharField("Сумма от 100 до 10000", max_length=255, blank=True)

    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Курс валют"
        verbose_name_plural = "Курсы валют"

    def __str__(self) -> str:
        return f' Обменик: {self.exchanger.address} '