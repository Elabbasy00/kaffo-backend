from django.db import models
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    cover = ResizedImageField(size=[500, 500], force_format="WEBP", quality=100, upload_to="blog/cover/")
    overview = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    content = RichTextUploadingField()

    def __str__(self) -> str:
        return self.overview
