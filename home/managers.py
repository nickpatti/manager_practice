from django.db import models


class ContentQuerySet(models.QuerySet):
    def get_page(self, page):
        return self.filter(page__title=page)


class ContentManager(models.Manager):
    def get_queryset(self):
        return ContentQuerySet(self.model, using=self._db)

    def get_page(self, page):
        return self.get_queryset().get_page(page)
