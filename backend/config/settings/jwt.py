import datetime

from config.env import env

# For more settings
# Read everything from here - https://styria-digital.github.io/django-rest-framework-jwt/#additional-settings

# Default to 7 days
JWT_EXPIRATION_DELTA_SECONDS = env("JWT_EXPIRATION_DELTA_SECONDS", default=60 * 60 * 24 * 7)
JWT_AUTH_COOKIE = env("JWT_AUTH_COOKIE", default="jwt")
JWT_AUTH_COOKIE_SAMESITE = env("JWT_AUTH_COOKIE_SAMESITE", default="Lax")
JWT_AUTH_HEADER_PREFIX = env("JWT_AUTH_HEADER_PREFIX", default="Bearer")
JWT_SECRET_KEY = env("JWT_SECRET_KEY", default="Bearer")


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(seconds=JWT_EXPIRATION_DELTA_SECONDS),
    # "REFRESH_TOKEN_LIFETIME": None,
    # "ROTATE_REFRESH_TOKENS": False,
    # "BLACKLIST_AFTER_ROTATION": False,
    "JWT_AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
    "JWT_AUTH_COOKIE_SECURE": False,  # Whether the auth cookies should be secure (https:// only).
    "JWT_AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
    "JWT_AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "JWT_AUTH_COOKIE_SAMESITE": JWT_AUTH_COOKIE_SAMESITE,
    "JWT_AUTH_COOKIE": JWT_AUTH_COOKIE,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": JWT_SECRET_KEY,
    "AUTH_HEADER_TYPES": (JWT_AUTH_HEADER_PREFIX,),
    "JWT_AUTH_COOKIE_SECURE": True,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": JWT_AUTH_COOKIE,
    "LOGIN_SERIALIZER": "src.authentication.serializers.CustomLoginSerializer",
    "USER_DETAILS_SERIALIZER": "src.authentication.serializers.CustomUserDetailsSerializer",
    "PASSWORD_RESET_SERIALIZER": "src.authentication.serializers.CustomPasswordResetSerializer",
}


ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
