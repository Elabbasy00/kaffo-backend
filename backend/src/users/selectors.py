from src.users.models import User


def user_get_login_data(*, user: User):
    return {
        "id": user.id,
        "email": user.email,
        "is_admin": user.is_admin,
        "is_superuser": user.is_superuser,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
    }
