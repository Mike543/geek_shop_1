from django.db import models

class ProductCategory(models.Model):# от models наследуем класс Model
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True#поле м.б. не заполнено
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(# внешний ключ – с чем связываем
        ProductCategory,
        on_delete=models.CASCADE # удаляем категорию – удаляются все ее элементы
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',#где будет лежать папка с картинками относительно корня
        blank=True
    )


    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        max_digits=8,# сколько цифр
        decimal_places=2,# сколько цифр после запятой
        verbose_name='цена',
    )

    quantity = models.PositiveIntegerField( # количество положительных значений
        verbose_name='количество на складе',
        default=0
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        ordering = ['-updated']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'