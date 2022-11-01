from django.shortcuts import render, redirect
from .forms import SignupForm

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
  return render(requeset, "accounts/index.html")