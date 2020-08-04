## Blog urls handling file

from django.urls import path
from . import views ## . is current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),   # pk is primary key of the post
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),   # pk is primary key of the post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),   # pk is primary key of the post
    path('about/', views.about, name="blog-about"),
]
