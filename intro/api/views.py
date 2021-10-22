import requests
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods


# 1. renderujemy pusty szablon.
# 2. tworzymy formularz w szablonie
# 3. obsługujemy dane w widoku

@require_http_methods(["GET", "POST"])
def fixer(request):

    amount = request.POST.get("amount")
    other = request.POST.get("other")

    if amount and other:
        res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d&",
                   params={"base": "eur", "symbols": other})

        # return HttpResponse(res.text) # To na początek, żeby zobaczyć czy w ogóle działa

        if res.status_code != 200:
            return HttpResponse("Cos poszło nie tak. Skontaktuj się z ...")

        data = res.json()

        if not data.get('success'):
            return HttpResponse(f"Coś poszło nie tak {data.get('error').get('type')}.")

        rate = data.get('rates').get(other.upper())
        result = round(float(amount) / rate, 2)
        return HttpResponse(f"Kantor wypłaca {result} euro.")

        # Mamy tutaj nieobsłużony jeden przypadek.
        # A co jeżeli rzutowanie się nie powiedzie. Trzeba wprowadzić
        # jakąś walidację wartości wprowadzanych do formularza.
        # W formularzu html możemy to zrobić na dwa sposoby:
        # 1. Na frontendzie (przed wysłaniem danych na serwer)
        # 2. Na backendzie (czyli po dojściu danych na serwer)

        # Na frontendzie możemy na dwa sposoby:
        # a. ustawiając odpowiedni typ inputu
        # b. js-em rejestrując odpowiedni callback na event submit naszego formularza

        # Na backendzie używając pythona

        # Zrobimy najprościej, czyli ustawiając odpowiedni typ inputu - number
        # Potem omawiamy w powietrzu jakby to było jsem:
        # Nasłuch na DOMContentLoaded, selector na formularz, podpinamy się pod event
        # onsubmit i piszemy callback -> (coś w nim robimy). Możemy zrobić taką walidację
        # na powtórzeniu z Frontendu za tydzień. W sumie to nie wiem co chcielibyście powtórzyć.
        # Jest coś takiego ?

        # A na serwerze w Pythonie to już wiadomo, mamy wiele możliwości.
        # Podstawowa kwestia: pytamy się czy możemy, czy się nie pytamy a jak nie wyjdzie prosimy o wybaczenie.

    return render(request, 'api/fixer.html')


@require_http_methods(["GET", "POST"])
def goodreads(request):
    # Analogicznie jak w przypadku fixer

    q = request.POST.get('q')
    if q:
        res = requests.get("https://www.goodreads.com/search.xml?key=1QM7Oy1POPeFEC6R9NWTA", params={"q": q})

        root = ET.fromstring(res.content)

        images = [item.text for item in root.findall('.search/results/work/best_book/image_url')]
        titles = [item.text for item in root.findall('.search/results/work/best_book/title')]

        books =[item for item in zip(titles, images)]

        return render(request, 'api/goodreads_result.html', {'books': books})

    return render(request, 'api/goodreads.html')