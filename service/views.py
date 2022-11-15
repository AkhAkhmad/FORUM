from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from service.models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


class RegisterForm(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_message = '%(username)s was created successfully'
    template_name = 'register.html'
    success_url = reverse_lazy('login')


# @login_required
# @permission_required('user.view_user', raise_exception=True)  # вывод ошибки, если нет прав
def index(req):
    return render(req, 'index.html')


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


# class CreatePostView(PermissionRequiredMixin, CreateView):  # PermissionRequiredMixin включает в себя LoginRequiredMixin
#     permission_required = 'service.added_post'  # вывод ошибки, если нет прав
#     model = Post
#     template_name = 'create_post.html'
#     form_class = PostForm
# fields = '__all__'

@login_required
@permission_required('service.add_post')
def create_post(req):
    form = PostForm()
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(req, f'Post {title} was creates successfully')
            return redirect('index')
    return render(req, 'create_post.html', {'form': form})


class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_post'
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'


class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_post'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm

    # def form_valid(self, form):
    #     form.instanсe.post_id = self.kwargs('pk')  # присваевает ключ из передаваемого параметра
    #     return super().form_valid(form)
