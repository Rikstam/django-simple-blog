from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class SinglePostView(DetailView):
    template = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts_tags"] = self.object.tags.all()
        return context


def get_date(post):
    """Get the date of the post"""
    return post["date"]
