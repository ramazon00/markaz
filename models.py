from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)


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
        ('dark', 'Dark'),
    )
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='media/posts', default='posts/default.png')
    status = models.CharField(max_length=50, choices=options, default='draft')
    status_color = models.CharField(max_length=50, choices=colors, default='primary')    
    objects = models.Manager()
    newmanager = NewManager()

    def get_absolute_url(self):
        return reverse('core:post_single', args = [self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

 