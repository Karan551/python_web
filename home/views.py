from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post


# Create your views here.
def home(request):
    return render(request, "home/index.html")


def contact(request):
    if request.method == "POST":
        # To get user details and remove extra spaces from both side
        name = request.POST["user_name"].strip()
        email = request.POST["email"].strip()
        phone = request.POST["contact-number"]
        content = request.POST["issue"].strip()
        # If user name is less than two or blank display alert messages
        if name == " " or len(name) <= 2:
            messages.error(request, "Please fill form correctly.")
        else:
            user_data = Contact(
                user_name=name,
                user_email=email,
                user_phoneNumber=phone,
                content=content,
            )
            user_data.save()
            messages.success(request, "Your issue has been submitted with us.")
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")


def search(request):
    query = request.GET["query"].strip()
    post = Post.objects.filter(title__icontains=query).first()
    print(post)
    context = {"post": post}
    return render(request, "home/search.html", context)
