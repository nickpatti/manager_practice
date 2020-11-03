from django.shortcuts import render
from django.contrib import messages
from .models import Content

# Create your views here.


def pages(request, page):
    posts = Content.objects.get_page(page)
    context = {
        'pages': posts
    }
    messages.info(request, 'this is the ' + page + 'view')
    return render(request, "home/pages.html", context)
