from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is a blog Home.")

def blog(request,slug):
    return HttpResponse(f'This is django blog {slug}')