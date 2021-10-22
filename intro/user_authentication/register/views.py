from django.shortcuts import render, redirect, reverse
from . import forms

# Create your views here.

# # v.1
# def register(request):
#     form = UserCreationForm()
#     return render(request, "register/register.html", {"form": form})

# # v.2
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     return render(request, "register/register.html", {"form": form})


# v.3
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("home"))
    else:
        form = forms.RegisterForm()
    return render(request, "registration/register.html", {"form": form})
