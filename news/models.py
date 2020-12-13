from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Link', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug':self.slug})

class News(models.Model):
    type_choices = (
        ('Business News', 'Business News'),
        ('News', 'News')
    )
    choose_type = models.CharField('Type of posts', max_length=50, choices=type_choices, null=True)
    title = models.CharField('Title', max_length=255)
    slug =  models.SlugField('Link', unique=True)
    image = models.ImageField('Image', upload_to='news/%Y/%m/%d/')
    description = models.TextField('Subtitle', blank=True)
    full_info = models.TextField('Info')
    image2 = models.ImageField('Next image', upload_to='news/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField('Date', default=timezone.now)
    popular = models.IntegerField('Views', default=0)    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True, related_name='categories')

    def __str__(self):
        return (f'{self.choose_type} || {self.title}')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'slug':self.slug})

class Ad(models.Model):
    type_choices = (
        ('Top Advertisement', 'Top Advertisement'),
        ('Avarage Advertisement', 'Avarage Advertisement')
    )
    choose_type = models.CharField('Type of advert', max_length=50, choices=type_choices, null=True)
    brand = models.CharField('Company name', max_length=255, blank=True)
    image = models.ImageField('Image', upload_to='Advertisement/%Y/%m/%d/', null=True)
    slug = models.URLField('Link to Company website')
    info = models.TextField('Info', blank=True)
    date = models.DateTimeField('Date', default=timezone.now)
    note = models.CharField('Note', max_length=255, null=True)


    def __str__(self):
        return self.note

    class Meta:
        verbose_name='Advertisement'
        verbose_name_plural='Advertisements'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField('Username', max_length=50)
    text = models.TextField('Изох', max_length=300)
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
