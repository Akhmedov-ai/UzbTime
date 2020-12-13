# Generated by Django 3.1.3 on 2020-12-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20201207_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type_news',
            options={'verbose_name': 'Type new', 'verbose_name_plural': 'Type news'},
        ),
        migrations.AddField(
            model_name='type_news',
            name='news',
            field=models.CharField(max_length=30, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='type_news',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, verbose_name='Subtitle'),
        ),
    ]