from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is a django Home.")

def contact(request):
    return HttpResponse("This is a django contact webpage.")

def about(request):
    return HttpResponse("This is a django about webpage.")
