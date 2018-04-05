# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebanner',
            name='image',
            field=models.ImageField(verbose_name='imagen del banner', upload_to='uploads/banner_image'),
        ),
        migrations.AlterField(
            model_name='imagebanner',
            name='image_size',
            field=models.CharField(choices=[('S', 'Pequeño'), ('M', 'Mediano'), ('B', 'Grande')], verbose_name='tamaño de la imágen', max_length=1, default='M'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image',
            field=models.ImageField(verbose_name='imágen', upload_to='uploads/product_image'),
        ),
        migrations.AlterField(
            model_name='imageproduct',
            name='image_size',
            field=models.CharField(choices=[('M', 'Celular'), ('S', 'Normal')], verbose_name='tamaño de la imágen', max_length=1, default='S'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_gender',
            field=models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre'), ('U', 'Unisex')], verbose_name='género del producto', max_length=1, default='U'),
        ),
    ]
