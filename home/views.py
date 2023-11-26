from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home/index.html')
    # return HttpResponse("This is a django Home.")

def contact(request):
    return render(request,'home/contact.html')
    # return HttpResponse("This is a django contact webpage.")

def about(request):
    return render(request,'home/about.html')
    # return HttpResponse("This is a django about webpage.")
