from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Yangilik
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Yangilik
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Yangilik
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Yangilik
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Yangilik
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Yangilik
    template_name = 'post_delete.html'
    succes_url = reverse_lazy('home')