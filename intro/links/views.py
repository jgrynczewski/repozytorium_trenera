from django.shortcuts import render

# 1. Widoki 1, 2 i zahardcodowanymi endpointami i bez nazw
# 2. widok 3 z parametrem
# 3. nazwy widoków i funkcja url


# Create your views here.
def first(request):
    return render(request, "links/first_view.html")

def second(request):
    return render(request, "links/second_view.html")

# Trzeci widok dorzucamy po skończeniu dwóch pierwszych.
def third(request, param):
    return render(request, "links/third_view.html", {"param": param})