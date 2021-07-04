from django.db import models


class ProductCategory(models.Model):
    objects = None
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name or f'Categoty with id - {self.pk}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    objects = None
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='категория',
        on_delete=models.CASCADE, )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='product_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=100,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='колличество товара на складе',
        default=0
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name or f'Product with id - {self.pk}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
