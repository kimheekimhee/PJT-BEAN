from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        forms = SignupForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("reviews:index")
    else:
        forms = SignupForm()
    context = {
        "forms": forms,
    }
    return render(request, "accounts/signup.html", context)


def index(request):
    return render(request, "accounts/index.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accoutns/login.html", context)
    else:
        return redirect("accounts:index")


def logout(request):
    auth_logout(request)
    return redirect("index")
