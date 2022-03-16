from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, "studentsite:student_home")

def login_view(request):
    if request.method == "POST":
       username = request.POST["username"] 
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
              login(request, user)
              return HttpResponseRedirect(reverse("studentsite:student_home"))
       else:
         return render(request, "loginsite/login.html", {
             "message": "Invalid Credentials."
            })

    return render(request, "loginsite/login.html")

def logout_view(request):
    logout(request)
    return render(request, "loginsite/login.html", {
        "message": "Logged out."
    })

def forgot(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("login"))
    
    return render(request, "loginsite/forgot.html")
    