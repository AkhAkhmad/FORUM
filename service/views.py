from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(req):
    return render(req, 'index.html')


def about(req):
    return render(req, 'about.html')


class ListPostView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = '-created_at'


class DetailPostView(DetailView):
    model = Post
    template_name = 'detail.post.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'create_post.html'
    # form_class = PostForm
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'

    # def form_valid(self, form):
    #     form.instanсe.post_id = self.kwargs('pk') # присваевает ключ из передаваемого параметра
    #     return super().form_valid(form)
