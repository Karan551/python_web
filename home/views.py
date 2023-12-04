from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User


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
    # If user query length is greater than 78 then show the alert.
    if len(query) > 78:
        # if query length is geater than 78 then create an empty queryset.
        allPost = Post.objects.none()
        messages.warning(
            request,
            "Your request was too large. Please Type appropriate keywords to find better result.",
        )
    else:
        post = Post.objects.filter(title__icontains=query)
        postAuthor = Post.objects.filter(author__icontains=query)
        postContent = Post.objects.filter(content__icontains=query)
        allPost = post.union(postContent, postAuthor)
    if len(allPost) == 0 and not len(query) > 78:
        messages.warning(
            request, "Sorry No matches found . Please make sure you type correct word."
        )
    context = {"post": allPost.first(), "query": query, "length": len(allPost)}
    return render(request, "home/search.html", context)


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST["user-input"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["user-email"]
        user_password = request.POST["user-password"]
        my_user = User.objects.create_user(username, email, user_password)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        return redirect("home")

    return HttpResponse("404 this page was not found")


def handleLogin(request):
    pass

def handleLogout(request):
    pass