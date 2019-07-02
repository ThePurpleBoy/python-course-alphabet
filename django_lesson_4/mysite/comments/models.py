from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from article.models import Article
from django.utils import timezone


class Comment(models.Model):

    author = models.CharField(max_length=30)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = RichTextUploadingField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



