
from .models import News, Category, ContactModel
from django.contrib import admin

@admin.register(News)
class NewsApdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'publish_time', 'status']
    filter_list = ['publish_time', 'status']
    prepopulated_fields = {'slug' : ('title',)}
    ordering = ['publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'name']


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

