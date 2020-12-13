# Generated by Django 3.1.3 on 2020-11-26 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20201123_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='ad',
            name='button',
            field=models.URLField(blank=True, verbose_name='Link in button'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=models.URLField(verbose_name='Link to Company website'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]