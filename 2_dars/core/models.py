from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    colors = (
        ('primary', 'Primary'),
        ('info text-dark', 'Info text-dark'),
        ('danger', 'Danger'),
        ('warning text-dark', 'Warning text-dark'),
    )

    title = models.CharField(max_length=200)
    summury = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    status = models.CharField(max_length=50, choices= options, default='published')
    status_color = models.CharField(max_length=50, choices= colors, default='primary')
    objects = models.Manager()
    newmanager = NewManager()

    def get_absolute_url(self):
        return reverse('core:post_single', args = [self.slug])

    class Meta():
        ordering = ('-published',) #tartib
    def __str__(self):
        return self.title
