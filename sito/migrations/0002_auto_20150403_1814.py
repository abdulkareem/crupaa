# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sito', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name_plural': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'Pagine'},
        ),
        migrations.AlterModelOptions(
            name='prodotti',
            options={'verbose_name_plural': 'Prodotti'},
        ),
        migrations.AlterField(
            model_name='immagini',
            name=b'croppingthumb',
            field=image_cropping.fields.ImageRatioField(b'image', '600x300', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='croppingthumb'),
        ),
    ]
