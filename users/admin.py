from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post']

