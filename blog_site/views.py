from django.shortcuts import render
from django.db import models

from .models import BlogPost


def index(request):
    latest_blog_posts = BlogPost.objects.order_by("id")
    context = {
        "latest_blog_posts": latest_blog_posts,
    }
    print(latest_blog_posts)
    return render(request, "blog_site/index.html", context)


def about(request):
    pass


def contact(request):
    pass


def post(request, blogpost_id):
    pass
