# Generated by Django 3.1.3 on 2020-12-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_ad_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_news',
            name='image',
            field=models.ImageField(upload_to='Ad news/%Y/%m/%d/', verbose_name='Image'),
        ),
    ]
