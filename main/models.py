from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    desc = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self) -> str:
        return self.title