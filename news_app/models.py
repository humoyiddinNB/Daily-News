from django.urls import reverse
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT
                              )

    class Meta:
        ordering = ["-publish_time"]
        verbose_name_plural = 'News'


    def get_absolute_url(self):
        return reverse('details', args=[self.slug])


    def __str__(self):
        return self.title




class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email



