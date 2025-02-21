from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name="article-detail"),
    path('add-post/', views.AddPostView.as_view(), name="add-post"),
    path('add-category/', views.AddCategoryView.as_view(), name="add-category"),
    path('article/edit/<int:pk>', views.UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete', views.DeletePostView.as_view(), name="delete-post"),
    path('category/<int:category_id>/', views.CategoryPostView.as_view(), name="category"),
    path('category-list/', views.CategoryListView.as_view(), name="category-list"),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name="add-comment"),
]
