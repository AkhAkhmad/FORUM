from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def index(req):
    return render(req, 'index.html')


@login_required
def about(req):
    return render(req, 'about.html')


class ListPostView(ListView):
    login_url = 'login'
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']


class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.post.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    # form_class = PostForm
    fields = '__all__'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instanсe.post_id = self.kwargs('pk') # присваевает ключ из передаваемого параметра
    #     return super().form_valid(form)