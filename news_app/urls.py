from django.urls import path
from .views import news_list, news_details, HomePageView, ContactViews, get_404, CategoryNewsListView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('all-news/', news_list, name='all_new'),
    path('details/<slug:news>/', news_details, name='details'),
    path('contact/', ContactViews.as_view(), name='contact'),
    path('404/', get_404, name='404'),
    path('news/category/<str:category_name>/', CategoryNewsListView.as_view(), name='category_news_list'),
]