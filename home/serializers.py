from rest_framework import serializers
from .models import Page, Content


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('title', )


class ContentSerializer(serializers.ModelSerializer):
    page = PageSerializer()

    class Meta:
        model = Content
        fields = ('id', 'page', 'secondary_title', 'text', 'objects')
