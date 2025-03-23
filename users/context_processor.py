from news_app.views import News


def news_list(request):
    all_news = News.objects.filter(status=News.Status.PUBLISHED)

    return {"news_list" : all_news}