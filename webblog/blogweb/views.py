from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogweb/index.htm', context)


class PostListView(ListView):
    model = Post
    template_name = 'blogweb/index.htm'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name= 'blogweb/post.htm'