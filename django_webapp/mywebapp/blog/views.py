from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#function based views
def home(request):
    post_content = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', post_content)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def login(request):
    return render(request, 'blog/login.html', {'title' : 'Login'})

#class based view
class PostListView(ListView):
    model = Post
    #retrieves the homepage
    template_name = 'blog/home.html'
    #gets page content
    context_object_name = 'posts'
    #sorts latest post first
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False
