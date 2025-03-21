from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import News, Category
from django.views import View
from django.views.generic import ListView


def news_list(request):
    all_news = News.objects.filter(status=News.Status.PUBLISHED)
    contex = {
        'news_list' : all_news
    }

    return render(request, 'news/news_list.html', contex)

def news_details(request, news):
    news = get_object_or_404(News, slug=news)
    news.views += 1
    news.save()
    context = {
        'news' : news
    }
    return render(request, 'news/single_page.html', context)


class HomePageView(ListView):
    model = News
    model1 = Category
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model1.objects.all()
        context['newses'] = self.model.objects.all().order_by('-publish_time')
        context['news_list'] = News.objects.filter(status=News.Status.PUBLISHED).order_by('-publish_time')
        context['local_news'] = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[:5]
        context['global'] = News.objects.all().filter(category__name='Xorij').order_by('-publish_time')[:5]
        context['technology'] = News.objects.all().filter(category__name='Texnologiya').order_by('-publish_time')[:5]
        context['sport'] = News.objects.all().filter(category__name="Sport").order_by('-publish_time')[:5]
        return context


class ContactViews(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'news/contact.html', {'form' : form})

    def post(self, request):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('contact')

        return render(request, 'news/contact.html', {'form' : form})



def get_404(request):
    context = {

    }
    return render(request, 'news/404.html', context)


class CategoryNewsListView(View):
    def get(self, request, category_name):
        news = News.objects.all().filter(category__name=category_name)
        return render(request, 'news/category.html', {'category_news' : news})


