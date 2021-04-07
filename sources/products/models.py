from django.db import models


def get_sentinel_category():
    return Category.objects.get_or_create(name='Uncategorized')[0]


class Category(models.Model):
    parent = models.ForeignKey(
        "self",
        related_name='parent_cat',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        verbose_name="Родительская категория"
    )
    name = models.CharField(max_length=200, verbose_name="Название категории")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        order_with_respect_to = 'parent'


class Mark(models.Model):
    name = models.CharField(max_length=60, verbose_name="Имя метки")
    
    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(
        "products.Category",
        related_name='category',
        on_delete=models.SET_DEFAULT,
        default=get_sentinel_category
    )
    ozone_id = models.CharField(max_length=200, verbose_name="Артикул OZONE")
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    update_date = models.DateTimeField(
        verbose_name='Время обновления',
        auto_now=True
    )
    price = models.IntegerField(verbose_name='Цена')
    marks = models.ManyToManyField('products.Mark', related_name='marks', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'