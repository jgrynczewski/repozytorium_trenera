from django.shortcuts import render
# Tworzymy dwa widoki i wskazujemy na powtórzenia.
# Potem przerabiamy na dziedziczenie

# Create your views here.
def first(request):
    return render(request, 'inheritance/first_view.html')

def second(request):
    return render(request, 'inheritance/second_view.html')