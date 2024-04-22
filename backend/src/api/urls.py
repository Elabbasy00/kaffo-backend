from django.urls import include, path

urlpatterns = [
    path("auth/", include(("src.authentication.urls", "authentication"))),
    path("users/", include(("src.users.urls", "users"))),
    path("education/", include(("src.education.urls", "education"))),
    path("blog/", include(("src.blog.urls", "blog"))),
]
