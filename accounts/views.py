from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import login as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


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
        forms = AuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            auth_login(request, forms.get_user())
            return redirect("accounts:index")
        else:
            forms = AuthenticationForm()
        context = {"forms": forms}
        return render(request, "accoutns/login.html", context)
    else:
        return redirect("accounts:index")


def logout(request):
    auth_logout(request)
    return redirect("index")


@login_required
def update(request):
    if request.method == "POST":
        forms = CustomUserChangeForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        forms = CustomUserChangeForm(instance=request.user)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/update.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        forms = PasswordChangeForm(request.user, request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:index")
    else:
        forms = PasswordChangeForm(request.user)
    context = {
        "forms": forms,
    }
    return render(request, "accounts/change_password.html", context)
