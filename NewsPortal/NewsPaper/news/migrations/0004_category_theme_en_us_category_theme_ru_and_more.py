# Generated by Django 4.2.1 on 2023-10-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_categorysubscribers_category_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='theme_en_us',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='theme_ru',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='article_text_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='article_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='headline_en_us',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='headline_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
