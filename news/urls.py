from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('category1/<slug:category>', views.index, name='category'),
    path('search/', views.search_result, name='search_results'),
    path('news/<slug:slug>', views.news_detail, name='news_detail_url'),
    path('register/', views.register, name='sign_up'),
    path('business-news/<slug:slug>', views.ad_news_detail, name='ad_news_detail_url'),
    path('category/<slug:slug>', views.category_detail, name='category_detail_url'),
    path('post/<slug:slug>/leave-comment', views.leave_comment, name='leave_comment')    
]