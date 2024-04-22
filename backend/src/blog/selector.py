from src.blog.models import Post
from src.common.utils import get_object


class BlogRepository:
    @staticmethod
    def get_all_post():
        return Post.objects.all()

    @staticmethod
    def get_single_post(*, slug: str):
        return get_object(Post, slug=slug)
