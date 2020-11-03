from rest_framework import viewsets, permissions
from .models import Content
from .serializers import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):
    # queryset = Content.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContentSerializer

    def get_queryset(self):
        page = self.kwargs.get('page')
        current_page = Content.objects.get_page(page)
        return current_page
