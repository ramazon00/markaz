# Generated by Django 4.1.6 on 2023-02-13 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('sammury', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, unique_for_date='publish')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=50)),
                ('status_color', models.CharField(choices=[('primary', 'Primary'), ('info text-dark', 'Info text-dark'), ('danger', 'Danger'), ('warning text-dark', 'Warning text-dark')], default='primary', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
