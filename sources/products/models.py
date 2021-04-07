from django.db import models


def get_sentinel_category():
    return Category.objects.get_or_create(name='Uncategorized')[0]


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='parent_cat', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Родительская категория")
    name = models.CharField(max_length=200, verbose_name="Название категории")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        #order_with_respect_to = 'parent'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE
        #on_delete=models.SET(get_sentinel_category())
    )
    ozone_id = models.CharField(max_length=200, verbose_name="Артикул")
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    update_date = models.DateTimeField(
        verbose_name='Время обновления',
        #auto_now_add=True,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'