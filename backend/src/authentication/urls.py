from django.urls import include, path

from .views import (
    # UserJwtLoginApi,
    # UserJwtLogoutApi,
    UserMeApi,
    UserSessionLoginApi,
    UserSessionLogoutApi,
    UserRegister,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path(
        "session/",
        include(
            (
                [
                    path("login/", UserSessionLoginApi.as_view(), name="login"),
                    path("logout/", UserSessionLogoutApi.as_view(), name="logout"),
                ],
                "session",
            )
        ),
    ),
    # path(
    #     "jwt/",
    #     include(
    #         (
    #             [
    #                 path("login/", UserJwtLoginApi.as_view(), name="login"),
    #                 path("logout/", UserJwtLogoutApi.as_view(), name="logout"),
    #             ],
    #             "jwt",
    #         )
    #     ),
    # ),
    path("me/", UserMeApi.as_view(), name="me"),
    path("register/", UserRegister.as_view(), name="register"),
]
