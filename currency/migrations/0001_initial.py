# Generated by Django 3.2.21 on 2023-11-08 07:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='usd', max_length=20, unique=True, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Exchanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('exchanger_info', models.CharField(blank=True, max_length=255)),
                ('telephone', models.CharField(help_text='+38096-123-45-67', max_length=16)),
                ('working_hours', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Обменик',
                'verbose_name_plural': 'Все Обменики',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Покупка')),
                ('sell', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Продажа')),
                ('sum', models.CharField(blank=True, max_length=255, verbose_name='Сумма от 100 до 10000')),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.currency')),
                ('exchanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.exchanger')),
            ],
        ),
    ]
