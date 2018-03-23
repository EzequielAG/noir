# -*- coding: utf-8 -*-
from decimal import Decimal

from django.db import models


class Product(models.Model):
    """Producto
    """

    code = models.CharField(u'código', max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(u'nombre', max_length=255)
    description = models.TextField(u'descripción')
    published = models.BooleanField(default=True, verbose_name=u'publicado')
    outstanding = models.BooleanField(default=False, verbose_name=u'destacado')
    category = models.ManyToManyField('CategoryProduct', verbose_name=u'categorías', blank=True)
    price = models.DecimalField(u'precio', max_digits=10, decimal_places=2, default=Decimal('0.00'))
    position = models.PositiveSmallIntegerField(db_index=True, blank=True, default=0,
                                                verbose_name=u'posición')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'producto'
        verbose_name_plural = u'productos'
        app_label = 'website'


class ImageProduct(models.Model):
    """Imágen del Producto
    """

    image = models.ImageField(u'imágen', upload_to='uploads/product_image')
    product = models.ForeignKey('Product', related_name='images')
    published = models.BooleanField(default=True, verbose_name=u'publicado')
    position = models.PositiveSmallIntegerField(db_index=True, blank=True, default=0,
                                                verbose_name=u'posición')

    class Meta:
        verbose_name = u'imágen de producto'
        verbose_name_plural = u'imágenes de productos'
        app_label = 'website'


class CategoryProduct(models.Model):
    """Categoría del Producto
    """

    name = models.CharField(u'nombre', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'categoría del producto'
        verbose_name_plural = u'categorías de los productos'
        app_label = 'website'


class ProductGender(models.Model):
    """Sexo a quien esta recomendado el producto
    """
    MUJER = 'M'
    HOMBRE = 'H'
    UNISEX = 'U'
    SEX_CHOICE = ((MUJER, 'Mujer'),
                  (HOMBRE, 'Hombre'),
                  (UNISEX, 'Unisex'))
    product_gender = models.CharField(u'género del producto', max_length=1,
                                      choices=SEX_CHOICE, default=UNISEX)
    product = models.OneToOneField('Product', verbose_name='producto')

    def __str__(self):
        return self.product_gender

    class Meta:
        verbose_name = u'género del producto'
        verbose_name_plural = u'géneros de los productos'
        app_label = 'website'


class ImageBanner(models.Model):
    """Imágen de los banners
    """

    SMALL = 'S'
    MEDIUM = 'M'
    BIG = 'B'

    SIZE_CHOICE = ((SMALL, 'Pequeño'),
                   (MEDIUM, 'Mediano'),
                   (BIG, 'Grande'))

    name = models.CharField(u'nombre de la imágen', max_length=255)
    title = models.CharField(u'titulo del banner', max_length=255, blank=True)
    text = models.TextField(u'texto del banner', blank=True)
    image = models.ImageField(u'imagen del banner', upload_to='uploads/banner_image')
    category = models.ForeignKey('ImageCategoryBanner', blank=True, verbose_name=u'lugar')
    image_size = models.CharField(u'tamaño de la imágen', max_length=1,
                                  choices=SIZE_CHOICE, default=MEDIUM)
    position = models.PositiveSmallIntegerField(db_index=True, blank=True, default=0)
    published = models.BooleanField(default=True, verbose_name=u'publicado')
    link = models.CharField(u'link', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'imágen banner'
        verbose_name_plural = u'imágenes banner'
        app_label = 'website'


class ImageCategoryBanner(models.Model):
    """Categoria del lugar de la imágen
    """

    place = models.CharField(u'lugar', max_length=255, unique=True)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = u'lugar del banner'
        verbose_name_plural = u'lugares de los banners'
        app_label = 'website'


class FAQ(models.Model):
    """Preguntas Frecuentes
    """

    ask = models.CharField(u'pregunta', max_length=255)
    answer = models.TextField(u'respuesta')
    position = models.PositiveSmallIntegerField(db_index=True, blank=True, default=0,
                                                verbose_name=u'posición')

    def __str__(self):
        return self.ask

    class Meta:
        verbose_name = u'pregunta frecuente'
        verbose_name_plural = u'preguntas frecuentes'
        app_label = 'website'


class Contact(models.Model):
    """Contacto
    """
    name = models.CharField(u'nombre', max_length=255)
    mail = models.EmailField(u'email')
    cell_phone = models.PositiveIntegerField(u'nro de celular', blank=True, null=True)
    message = models.TextField(u'mensaje')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'contacto'
        verbose_name_plural = u'contactos'
        app_label = 'website'
