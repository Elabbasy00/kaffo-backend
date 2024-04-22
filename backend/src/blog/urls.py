from django.urls import path
from src.blog.views import GetPostsViews, GetSinglePostView

urlpatterns = [
    path("list/", GetPostsViews.as_view(), name="blog-list"),
    path("single-post/", GetSinglePostView.as_view(), name="single-post"),
]
