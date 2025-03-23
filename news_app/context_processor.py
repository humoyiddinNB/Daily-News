from .models import News, Category
from django.shortcuts import get_object_or_404



def latest_news(request):
    latest_news = News.objects.all().order_by("publish_time")[:10]
    categories = Category.objects.all()
    context = {
        'latest_news' : latest_news,
        'categories' : categories
    }
    return context

def popular_posts(request):
    popular_posts = News.objects.all().order_by("-views")[:4]
    return {"popular_posts" : popular_posts}

