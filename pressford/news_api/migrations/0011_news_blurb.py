# Generated by Django 2.0.4 on 2018-04-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0010_news_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='blurb',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]