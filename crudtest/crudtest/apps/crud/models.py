from django.db import models
from datetime import date


class Products(models.Model):
    title = models.CharField('Наименование товара', max_length=150)
    price = models.PositiveIntegerField('Цена товара (руб.)')  # положительное значение от 0 до 22к
    description = models.TextField('Описание товара')
    url = models.CharField('Ссылка на товар', max_length=160)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
