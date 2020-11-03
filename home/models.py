from django.db import models
from .managers import ContentManager
# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Content(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page')
    secondary_title = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    objects = ContentManager()
