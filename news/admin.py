from django.contrib import admin
from .models import News, Ad, Category, Comment
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ad)