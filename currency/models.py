from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

class Currency(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    exchanger_info = models.CharField(max_length=255)
    buy_usd = models.FloatField()
    sell_usd = models.FloatField()
    buy_eur = models.FloatField()
    sell_eur = models.FloatField()
    working_hours = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title