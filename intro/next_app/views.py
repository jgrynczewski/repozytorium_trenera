import datetime

from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Witaj, świecie!")


def hi(request):
    return render(request, 'next_app/hi.html')


def parameters(request, param):

    # Bezpieczeństwo aplikacji.

    # Przy przyjmowaniu jakichkolwiek danych od użytkownika
    # należy pamiętać o ich oczyszczeniu/odkarzeniu (sanitize).
    # W ten sposób zabezpieczamy się przed wszelkiego rodzaju atakami typu injection
    # Pewnie słyszeliście już o sql injection.
    # Ale istnieje wiele innych: shell injection, html injection

    # Popatrzmy na html injection (czyli wstrzykiwanie html)
    # http://127.0.0.1:8000/next/3/<h2 style="color:red;">John</h2>
    # Nie zadziała bo slash, ale przeglądarka jest wybaczająca
    # bez zamykającego slasha też spróbuje wykonać co się da.
    # 127.0.0.1:8000/next/3/<h2 style="color: red;">John

    # 127.0.0.1:8000/next/3/<a href="https://www.google.pl">a
    # Tu znowu się nie wykona, bo slashe
    # Ale przeglądarki rozumieją też backslashe
    # https:\\www.google.pl
    # Próbujemy
    # 127.0.0.1:8000/next/3/<a href="https:\\www.google.pl">a
    # Nie zadziałało, bo przeglądark od razu podmieniła backslashe na slashe
    # To może użyć kodowania ?
    # Każdy znak ma odpowiadający mu znak, który przeglądarka będzie umiała
    # zinterprować (bo ma zaimplementowanie kodowanie unicode)
    # w szczególności backslash to %5C
    # Czegoś takiego przegląrka nie powinna podmienić
    # 127.0.0.1:8000/next/3/<a href="https:%5C%5Cwww.google.pl">a

    # W przypadku JS mówimy o podatności Cross-Site Scripting (XSS)
    # 127.0.0.1:8000/next/3/<a onmouseover=alert("Hi!");>John/

    # Co nam po tym ?
    # Możemy gdzieś podrzucić taki link (np. wysłać na maila) i jeżeli
    # użytkownik kliknie na ten link atak zostanie wykonany za pomocą
    # obcego klienta (będziemy niezauważalni).

    # Jak się zabezpieczyć ? Na przykład:
    # from markupsafe import escape
    # print(param)
    # sanitize_param = escape(param)
    # print(sanitize_param)

    return HttpResponse(f"Hello {param}")


# Przekazywanie zmiennych do szablonu
def templates(request):
    name = "Jan"
    return render(request, 'next_app/4.html', {"name":name})


# Parametr od użytkownika przekazywany do szablonu
def templates2(request, param):
    # Tu nam się już nie uda injection, ponieważ Jinja domyślnie ucieka z wartościami
    # przekazywanych parametrów. Żeby pozostawiła surowe znaki trzeba użyć specjalnego filtra
    # (o filtrach w Jinjy powiemy później).
    return render(request, 'next_app/5.html', {"param":param})


def is_it_monday(request):
    """Jinja conditions"""

    now = datetime.datetime.now()
    # 0-monday, 6-sunday
    is_monday = True if now.day == 0 else False

    return render(
        request,
        'next_app/isitmonday.html',
        {"is_monday": is_monday}
    )


def fruit(request):
    """Jinja loops"""
    fruits = ['jabłko', 'banan', 'winogrona', 'mandarynki']
    d = {
        "owoc": "jabłko",
        "wiek": 40,
    }

    return render(
        request,
        'next_app/fruit.html',
        {
            "fruits": fruits,
            "text": "<h1 style='color:red;'>ala</h1>",
            "a_dict": d,
        }
    )
