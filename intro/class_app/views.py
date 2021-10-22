# WIDOKI KLASOWE I WIDOKI GENERYCZNE

from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.views import View
from django.shortcuts import get_object_or_404
from class_app.models import Person
from django.views.generic import DetailView
from class_app.forms import PersonForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")

# Dorabiamy model Person
# Zróbmy widok, który wyświetli nam szczegóły wskazanego wpisu z tabelki.
# function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)
    return render(request, 'class_app/person_detail.html', {"person": p})


# class-based view
class PersonView(View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(request, 'class_app/person_detail.html', {"person": p})

# Generic view
class PersonDetailView(DetailView):
    model = Person
    # No i szablon
    # DetailView szuka szablony o nazwie person_detail.html

    # I tyle.
    # Gdybyśmy chcieli zacząć coś zmieniać, musielibyśmy wejść w szczegóły.
    # https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-display/#detailview

    # Gdybyśmy potrzebowali przekazać coś do kontekstu używamy funkcji get_context_data
    # def get_context_data(self, **kwargs):
    #     # w kwargs jest już nasz obiekt (możemy wyprintować)
    #     # print(kwargs)
    #     # Tu widzimy, że obiekt przekazujemy w kontekście pod nazwą object.
    #     # kwargs to nasz kontekst, tu możemy go dowolne modyfikować.
    #     kwargs['imie'] = "Ala"
    #     context = super(DetailView, self).get_context_data(**kwargs)
    #     return context

    # Nazwa szablony przechowywana jest w zmiennej template_name
    # Domyślnie
    # template_name = "class_app/person_detail.html"
    # Możemy zmienić na
    # template_name = "class_app/test.html" # + zmienić nazwę szablonu i sprawdzić.
    # Nazwę szablonu możemy przekazać też w funkcji as_view w dyspozytorze urli
    # views.PersonView.as_view(template_name="class_app/test.html")
    # Wracamy do domyślnej nazwy.

# Popatrzmy jeszcze na inny widok (tym razem z formularzem
# function-based view
def create_person(request):
    if request.method == "GET":
        form = PersonForm()

        return render(request, 'class_app/create-person.html', {"form": form})

    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse('class_app:hello2'))


# Class-based view
class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'class_app/create-person.html', {
            "form": form
        })

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('class_app:hello2'))


# Generic view
class PersonCreateView2(CreateView):
    # CreateView szuka szablonu person_form.html
    model = Person
    fields = '__all__'
    # Będzie błąd - czytamy co zrobić i poprawiamy to w modelu
    # get_absolute_url

# I wiele innych, przygotowanych wioków:
# https://docs.djangoproject.com/en/3.1/ref/class-based-views/
# Każdy ma jakieś swoje szczegóły.
