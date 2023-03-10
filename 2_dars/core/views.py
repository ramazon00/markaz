from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.models import User
def home(request):

    all_posts = Post.objects.all()


    return render(request, 'home.html', {'posts' : all_posts})

def post_single(request, post):

    post = get_object_or_404(Post, slug=post, status='publish')
    return render(request, 'single.html', {'post' : post})

def user(request):

    users = User.objects.all()

    return render(request, 'user.html', {'posts' : users})

class AddView(CreateView):
    model = Post
    template_name = 'add.html'
    pk_url_kwarg = 'pk'
    fields = '__all__'
    succes_url = reverse_lazy('core:home')

class EditView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    succes_url = reverse_lazy('core:home')

class Delete(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    succes_url = reverse_lazy('core:home')
    template_name = 'confirm-delete.html'