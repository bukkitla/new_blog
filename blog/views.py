from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

# posts=Post.objects.all()
#
# title='Homepage'
# context={'posts':posts,'title':title}
#
# def home(request):
#
#     return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class CreatePotView(LoginRequiredMixin,CreateView):
    login_url = '/login/'

    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = '/login/'

    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    paginate_by = 2

    def get_queryset(self):
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)
