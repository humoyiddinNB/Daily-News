import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from users.forms import CommentCreateForm, CommentUpdateForm
from users.models import Comment
from .forms import ContactForm
from .models import News, Category
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView


def get_date():
    return datetime.datetime.today()


def news_list(request):
    all_news = News.objects.filter(status=News.Status.PUBLISHED)
    contex = {
        'news_list' : all_news
    }

    return render(request, 'news/news_list.html', contex)

def news_details(request, slug):
    news = get_object_or_404(News, slug=slug)
    newses = News.objects.all().filter(category__name=news.category)[1:4]
    categories = Category.objects.all()
    comments = Comment.objects.filter(post__slug=news.slug)[:5]
    form = CommentCreateForm(request.POST)
    if form.is_valid() and request.POST:
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = news
        comment.save()
        return redirect('details', slug=news.slug)

    news.views += 1
    news.save()
    context = {
        'news' : news,
        'newses' : newses,
        'categories' : categories,
        'comments' : comments,
        'form' : form
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




@method_decorator(login_required, name='dispatch')
class CommentUpdateView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.content = request.POST.get("content")
            comment.save()
            return JsonResponse({"success": True, "content": comment.content})
        return JsonResponse({"success": False}, status=403)

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False}, status=403)

@login_required
def add_comment(request, slug):
    if request.method == "POST":
        news = get_object_or_404(News, slug=slug)
        content = request.POST.get("content")
        comment = Comment.objects.create(user=request.user, news=news, content=content)
        return JsonResponse({"success": True, "comment_id": comment.id})
    return JsonResponse({"success": False}, status=400)