# Generated by Django 4.2.6 on 2023-11-08 13:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='confirmation_comment',
            field=models.BooleanField(default=False, verbose_name='Подтверждение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_post',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент'),
        ),
    ]
