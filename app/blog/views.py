from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.


def get_date(post):
    """Get the date of the post"""
    return post["date"]


def index(request):
    """Get last 3 posts"""
    posts_list = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": posts_list})


def posts(request):
    """Get all posts"""
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    """Get a single post"""
    post = get_object_or_404(Post, slug=slug)
    post_tags = post.tags.all()
    return render(request, "blog/post-detail.html", {
        "post": post,
        "tags": post_tags
        })
