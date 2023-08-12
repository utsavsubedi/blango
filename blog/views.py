from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    print('all posts: ',all_posts)
    return render(request, "blog/index.html")