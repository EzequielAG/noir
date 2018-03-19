# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('mail', models.EmailField(max_length=254, verbose_name='email')),
                ('cell_phone', models.PositiveIntegerField(verbose_name='nro de celular', blank=True)),
                ('message', models.TextField(verbose_name='mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ask', models.CharField(max_length=255, verbose_name='pregunta')),
                ('answer', models.TextField(verbose_name='respuesta')),
                ('position', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='posici\xf3n', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='nombre de la imagen')),
                ('title', models.CharField(max_length=255, verbose_name='titulo del banner', blank=True)),
                ('text', models.TextField(verbose_name='texto del banner', blank=True)),
                ('product_gender', models.CharField(default=b'M', max_length=1, verbose_name='tama\xf1o de la imagen', choices=[(b'S', b'Peque\xc3\xb1o'), (b'M', b'Mediano'), (b'B', b'Grande')])),
                ('position', models.PositiveSmallIntegerField(default=0, db_index=True, blank=True)),
                ('published', models.BooleanField(default=True, verbose_name='publicado')),
                ('link', models.CharField(max_length=200, verbose_name='link', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageCategoryBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(unique=True, max_length=255, verbose_name='lugar')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255, unique=True, null=True, verbose_name='c\xf3digo', blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('published', models.BooleanField(default=True, verbose_name='publicado')),
                ('outstanding', models.BooleanField(default=False, verbose_name='destacado')),
                ('price', models.DecimalField(default=Decimal('0.00'), verbose_name='precio', max_digits=10, decimal_places=2)),
                ('position', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='posici\xf3n', blank=True)),
                ('category', models.ManyToManyField(to='website.CategoryProduct', verbose_name='categor\xedas', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_gender', models.CharField(default=b'U', max_length=1, verbose_name='genero del producto', choices=[(b'M', b'Mujer'), (b'H', b'Hombre'), (b'U', b'Unisex')])),
                ('product', models.OneToOneField(verbose_name=b'producto', to='website.Product')),
            ],
        ),
        migrations.AddField(
            model_name='imagebanner',
            name='category',
            field=models.ForeignKey(to='website.ImageCategoryBanner', blank=True),
        ),
    ]
