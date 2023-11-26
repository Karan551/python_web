from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'blog/blogHome.html')
    # return HttpResponse("This is a blog Home.")

def blog(request,slug):
    return render(request,'blog/blogPost.html')
    # return HttpResponse(f'This is django blog {slug}')