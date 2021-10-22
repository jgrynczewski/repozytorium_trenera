# FORMULARZE DJANGO i FORMULARZE MODELU

from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm
from .forms import MessageForm

from form_app4.models import Message

# Najpierw oglądamy panel administratora.
# Potem tworzymy aplikację
# Potem tworzymy model do którego będziemy zapisywali dane i rejestrujemy go w panelu.
# Pokazujemy gotowy formularz (CRUD) w panelu.
# Potem zaczynamy robić własne formularze.

# HTML form - dotychczasowy sposób pracy z formularzami
def contact1(request):
    if request.method == "POST":
        print(request.POST)

        data = request.POST
        Message.objects.create(
            name=data.get('name'),
            email = data.get('email'),
            category = data.get('category'),
            subject = data.get('subject'),
            body = data.get('body')
        )

    # Co z walidacją takiego formularza ?
    # Na froncie część załatwi użycie odpowiedniego pola
    # reszta za pomocą js.
    # Na backendzie Python.
    return render(request, 'form_app4/form1.html')

# Django form
def contact2(request):
    if request.method == "POST":
        form = ContactForm(request.POST) # bound form
        if form.is_valid():

            # print(form.cleaned_data)
            # Konwertuje dane do zunifikowanego pythonowego formatu,
            # np. datatime field zawsze będzie konwertowany
            # do datetime.datetime object, nieważne jakiego widgetu użyjemy.
            # przed validacją (is_valid()) cleaned_data będzie zawierał tylko
            # te dane
            data = form.cleaned_data
            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body')
            )

    form = ContactForm() # unbound form
    # return HttpResponse("OK") # Na sprawdzenie, czy wszystko
    # dobrze skonfigurowane
    return render(request, 'form_app4/form2.html', {
        "form": form
    })


# Django form - Model Form (formularz dla modelu)
def contact3(request):
    if request.method == "POST":
        form = MessageForm(request.POST) # bound form
        # walidacja wbudowana
        form.save()

    form = MessageForm() # unbound form
    # return HttpResponse("OK") # Na sprawdzenie, czy wszystko
    # dobrze skonfigurowane
    return render(request, 'form_app4/form3.html', {
        "form": form
    })

