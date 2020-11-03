from rest_framework import routers
from .api import ContentViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register('', ContentViewSet, 'content')

urlpatterns = [
    path('<page>/', views.pages, name='pages'),
    path('api/<page>/', include(router.urls)),
]
