from django.shortcuts import render, redirect, reverse
from .models import News, Ad, Category, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .forms import RegisterForm

# Create your views here.

def index(request, category=None):
    news = News.objects.all()
    #   news = news.filter(category__slug=category) if category else news
    last_news = news.filter(choose_type='News').order_by('-created_at')[:4]
    secondary_news = news.filter(choose_type='News').order_by('-created_at')[4:10]
    all_news = news.filter(choose_type='News').order_by('-created_at')[10:30]
    advert = Ad.objects.filter(choose_type='Top Advertisement').all().order_by('-date')[:1]
    ad = Ad.objects.filter(choose_type='Avarage Advertisement').all().order_by('-date')[:1]
    category = Category.objects.all()
    news_ad = news.filter(choose_type='Business News').order_by('-created_at')[:4]
    return render(
        request, 'news/index.html', 
        {'all_news':all_news, 'news_ad': news_ad, 'ad':ad,'advert':advert,
        'category':category,'secondary_news':secondary_news,'last_news':last_news}
    )
    
def news_detail(request, slug):
    news = News.objects.get(slug__iexact=slug)
    news.popular += 1
    news.save()
    advert = Ad.objects.filter(choose_type='Top Advertisement').all().order_by('-date')[:1]  
    news_ad = News.objects.filter(choose_type='Business News').all().order_by('-created_at')[:3]
    return render(request, 'news/news_detail.html', {'news':news,'advert':advert,'news_ad':news_ad})

def ad_news_detail(request, slug):
    news = News.objects.get(slug__iexact=slug)
    news.popular += 1
    news.save()
    advert = Ad.objects.filter(choose_type='Top Advertisement').all().order_by('-date')[:1]
    news_ad = News.objects.filter(choose_type='Business News').all().order_by('-created_at')[:3]
    return render(request, 'news/ad_news_detail.html', {'news':news,'advert':advert,'news_ad':news_ad})

def search_result(request):
    query = request.GET.get('search')
    advert = Ad.objects.filter(choose_type='Top Advertisement').all().order_by('-date')[:1]
    category = Category.objects.all()
    news_ad = News.objects.filter(choose_type='Business News').all().order_by('-created_at')[:4]   
    search_obj = News.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(full_info__icontains=query), choose_type='News').order_by('-created_at')
    return render(request, 'news/search_results.html', {'search_obj':search_obj,'category':category,'advert':advert,'news_ad':news_ad})

def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    all_category = Category.objects.all()
    news = News.objects.all()
    news_ad = News.objects.filter(choose_type='Business News').all().order_by('-created_at')[:4]
    advert = Ad.objects.filter(choose_type='Top Advertisement').all().order_by('-date')[:1]
    return render(request, 'news/category_detail.html', {'category': category,'all_category':all_category, 'news': news, 'news_ad':news_ad, 'advert':advert})

def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form':form})

def leave_comment(request, slug):
    try:
        post = News.objects.get(slug__iexact=slug) 
    except:
        raise Http404('Post not found')
    if request.user.is_authenticated:
        user = request.user.username
        post.comments.create(username=request.POST.get('username'), text=request.POST.get('text'))

    else:
        post.comments.create(username=request.POST.get('username'), text=request.POST.get('text'))
        comment = Comment.objects.order_by('-date_pub')[:2]
    return HttpResponseRedirect(reverse('news_detail_url', args=(post.slug,)))
