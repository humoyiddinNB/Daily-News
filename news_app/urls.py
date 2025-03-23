from django.urls import path
from .views import news_list, news_details, HomePageView, ContactViews, get_404, CategoryNewsListView, \
    CommentUpdateView, CommentDeleteView, add_comment

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('all-news/', news_list, name='all_new'),
    path('details/<slug:slug>/', news_details, name='details'),
    path('contact/', ContactViews.as_view(), name='contact'),
    path('404/', get_404, name='404'),
    path('category/<str:category_name>/', CategoryNewsListView.as_view(), name='category'),
    path('comment/update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:comment_id>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/add/<slug:slug>/', add_comment, name='comment_add'),
]