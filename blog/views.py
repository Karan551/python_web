from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    return render(request, "blog/blogHome.html", context)


def blog(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {"post": post}
    return render(request, "blog/blogPost.html", context)
    # return HttpResponse(f'This is django blog {slug}')