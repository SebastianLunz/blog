from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, CategoryForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-post_date']


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'


class CategoryPostView(DetailView):
    model = Category
    template_name = 'blog/categories.html'
    pk_url_kwarg = "category_id"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_post"] = Post.objects.filter(category=self.kwargs['category_id'])
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article-detail', args=[self.kwargs['pk']])


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "blog/add_category.html"

    success_url = reverse_lazy('blog:category-list')


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:index')
