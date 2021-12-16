from datetime import date
from django.shortcuts import render

# Create your views here.

posts_list = [
    {
        "slug": "hike-in-the-mountains",
        "image": "image-1.jpg",
        "author": "Riku",
        "date": date(2021, 6, 6),
        "title": "Hike in the mountains",
        "excerpt": "Culpa id ex deserunt enim est aliquip. Ea sit sunt pariatur ullamco laboris nulla commodo labore exercitation Lorem ex.",
        "content": """
            Tempor in consequat voluptate culpa. Labore nostrud ex tempor tempor. Qui excepteur in in commodo minim ullamco eu exercitation nulla. Amet do mollit nulla dolor et. 
            Consectetur et occaecat aute cillum mollit voluptate consectetur aliquip sit.
            Commodo cupidatat elit deserunt culpa officia aliqua mollit non sit duis. Veniam adipisicing deserunt nisi deserunt anim mollit do elit occaecat anim elit ex nostrud sunt. 
            Ad veniam Lorem pariatur consequat adipisicing voluptate. Enim magna anim consectetur mollit laborum do. Irure labore duis est aliqua cillum cupidatat do consectetur in. 
            Nostrud minim non nostrud dolore dolor quis dolore.
        """,
    },
    {
        "slug": "hike-in-the-river",
        "image": "image-2.png",
        "author": "Riku",
        "date": date(2021, 7, 7),
        "title": "Hike in the river",
        "excerpt": "Culpa id ex deserunt enim est aliquip. Ea sit sunt pariatur ullamco laboris nulla commodo labore exercitation Lorem ex.",
        "content": """
            Tempor in consequat voluptate culpa. Labore nostrud ex tempor tempor. Qui excepteur in in commodo minim ullamco eu exercitation nulla. Amet do mollit nulla dolor et. 
            Consectetur et occaecat aute cillum mollit voluptate consectetur aliquip sit.
            Commodo cupidatat elit deserunt culpa officia aliqua mollit non sit duis. Veniam adipisicing deserunt nisi deserunt anim mollit do elit occaecat anim elit ex nostrud sunt. 
            Ad veniam Lorem pariatur consequat adipisicing voluptate. Enim magna anim consectetur mollit laborum do. Irure labore duis est aliqua cillum cupidatat do consectetur in. 
            Nostrud minim non nostrud dolore dolor quis dolore.
        """,
    },
    {
        "slug": "hike-in-the-forest",
        "image": "image-2.png",
        "author": "Riku",
        "date": date(2021, 8, 8),
        "title": "Hike in the Forest",
        "excerpt": "Culpa id ex deserunt enim est aliquip. Ea sit sunt pariatur ullamco laboris nulla commodo labore exercitation Lorem ex.",
        "content": """
            Tempor in consequat voluptate culpa. Labore nostrud ex tempor tempor. Qui excepteur in in commodo minim ullamco eu exercitation nulla. Amet do mollit nulla dolor et. 
            Consectetur et occaecat aute cillum mollit voluptate consectetur aliquip sit.
            Commodo cupidatat elit deserunt culpa officia aliqua mollit non sit duis. Veniam adipisicing deserunt nisi deserunt anim mollit do elit occaecat anim elit ex nostrud sunt. 
            Ad veniam Lorem pariatur consequat adipisicing voluptate. Enim magna anim consectetur mollit laborum do. Irure labore duis est aliqua cillum cupidatat do consectetur in. 
            Nostrud minim non nostrud dolore dolor quis dolore.
        """,
    },
]


def get_date(post):
    return post["date"]


def index(request):
    sorted_posts = sorted(posts_list, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = posts_list
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def post_detail(request, slug):
    post = next(post for post in posts_list if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": post})
