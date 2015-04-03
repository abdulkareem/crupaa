# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aziende',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('denominazione', models.CharField(max_length=100, verbose_name=b'Denominazione:')),
                ('email', models.CharField(max_length=100, null=True, verbose_name=b'E-mail:', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, verbose_name=b'Telefono:', blank=True)),
                ('Fax', models.CharField(max_length=100, null=True, verbose_name=b'Fax:', blank=True)),
                ('web', models.CharField(max_length=100, null=True, verbose_name=b'Sito Web:', blank=True)),
                ('nazione', models.CharField(max_length=100, null=True, verbose_name=b'Nazione:', blank=True)),
                ('indirizzo', models.CharField(max_length=100, null=True, verbose_name=b'indirizzo:', blank=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'cap:', blank=True)),
                ('citta', models.CharField(max_length=100, null=True, verbose_name=b'citta:', blank=True)),
                ('piva', models.CharField(max_length=100, null=True, verbose_name=b'Piva:', blank=True)),
                ('codfisc', models.CharField(max_length=100, null=True, verbose_name=b'CodiceFiscale:', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Partner Aziende/Marchi Commerciati',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo:')),
                ('titolo_fr', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Francese:', blank=True)),
                ('titolo_uk', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Inglese:', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Immagini',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('didascalia', models.TextField(null=True, blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slidepage', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slidepage')),
                (b'croppingthumb', image_cropping.fields.ImageRatioField(b'image', '600x450', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingthumb')),
                (b'croppingslide', image_cropping.fields.ImageRatioField(b'image', '1140x487', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingslide')),
                (b'croppingcarousel', image_cropping.fields.ImageRatioField(b'image', '198x132', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingcarousel')),
                (b'freecropping', image_cropping.fields.ImageRatioField(b'image', '1200x1125', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name=b'Freecropping')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'Galleria Immagini',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('titolo_fr', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Francese:', blank=True)),
                ('titolo_uk', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Inglese:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('body_fr', models.TextField(null=True, verbose_name=b'Descrizione Francese', blank=True)),
                ('body_uk', models.TextField(null=True, verbose_name=b'Descrizione Inglese', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                (b'croppingminiatura', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Miniatura')),
                (b'croppingslider', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Slider Revolution')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Cropping')),
                (b'croppingfree', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name=b'Free Crop')),
                ('video', models.CharField(max_length=100, null=True, verbose_name=b'Video:', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('galleria', models.ManyToManyField(to='sito.Immagini', null=True, verbose_name=b'Seleziona Immagini Galleria', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prodotti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, null=True, verbose_name=b'Titolo:', blank=True)),
                ('titolo_fr', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Francese:', blank=True)),
                ('titolo_uk', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Inglese:', blank=True)),
                ('body', models.TextField(null=True, verbose_name=b'Descrizione', blank=True)),
                ('body_fr', models.TextField(null=True, verbose_name=b'Descrizione Francese', blank=True)),
                ('body_uk', models.TextField(null=True, verbose_name=b'Descrizione Inglese', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                (b'croppingminiatura', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Miniatura')),
                (b'croppingslider', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Slider Revolution')),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name=b'Cropping')),
                (b'croppingfree', image_cropping.fields.ImageRatioField(b'image', '500x469', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=True, adapt_rotation=False, help_text=None, verbose_name=b'Free Crop')),
                ('video', models.CharField(max_length=100, null=True, verbose_name=b'Video:', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('categoria', models.ForeignKey(blank=True, to='sito.Categorie', null=True)),
                ('galleria', models.ManyToManyField(to='sito.Immagini', null=True, verbose_name=b'Seleziona Immagini Galleria', blank=True)),
                ('marchio', models.ForeignKey(blank=True, to='sito.Aziende', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=100, verbose_name=b'Titolo del Progetto:')),
                ('titolo_fr', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Francese:', blank=True)),
                ('titolo_uk', models.CharField(max_length=100, null=True, verbose_name=b'Titolo Inglese:', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('active', models.BooleanField(default=False)),
                ('didascalia', models.TextField(null=True, blank=True)),
                ('didascalia_fr', models.TextField(null=True, verbose_name=b'Didascalia Francese', blank=True)),
                ('didascalia_uk', models.TextField(null=True, verbose_name=b'Didascalia Inglese', blank=True)),
                (b'cropping', image_cropping.fields.ImageRatioField(b'image', '1170x500', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                (b'slidepage', image_cropping.fields.ImageRatioField(b'image', '870x480', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='slidepage')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name_plural': 'Slider in Homepage',
            },
        ),
    ]
