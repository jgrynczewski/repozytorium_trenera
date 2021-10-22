from django.shortcuts import HttpResponse
from django.shortcuts import render

# Cookies to termin związany z przeglądarką (klientem)
# Sesja to koncept związany z serwerem.
# Sesje wykorzystują ciasteczka do identyfikacji, do której sesji piszemy.
# Jednym z podstawowych zastosowań ciasteczek jest utworzenie i podtrzymywanie sesji.

# Create your views here.
def cookies(request):
    # print(dir(request))
    print(request.COOKIES)
    res = HttpResponse("OK")
    res.set_cookie("ciasteczko1", 5)
    res.set_cookie("ciasteczko2", 10, max_age=1000)  # liczba sekund do wygaśnięcia
    return res


# Sesja - mechanizm opierający się na ciasteczkach.
def session(request):
    # # print(dir(request)) # Znajdujemy obiekt sesji
    # # print(dir(request.session)) # Patrzym co potrafi
    # print(request.session_session_key) # None -> bo nie utworzyliśmy żadnej sesji.
    # Patrzymy co potrafi obiekt session - _get_or_create_session_key()
    # sessionId = request.session._get_or_create_session_key()
    # print(request.session.session_key)
    # res = HttpResponse("OK")
    # res.set_cookie("sessionid", sessionId)
    # No ale wciąż nic. Bo nie wszystko zrobiliśmy.
    # Teraz należałoby jeszcze zapisać tą zmienną w bazie danych.
    # Wcześniej stworzyć tabelkę z kolumnami id i powiązane z id dane.
    # zahashować dane (bo mogą być wrażliwe, np. hasło, zakodowane base64 -> można odszyfrować base64.b64decode).
    # I porównywać klucz z wartością w tabelce. Jeżeli istnieje to to, jeżeli nie to tamto.

    # Ale mamy session middleware, które za nas to wszystko robi.
    # Wystarczy, że zaczniemy pisać do sesji, a uruchomi się cała ta logika.
    num_visit = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num_visit
    return HttpResponse(f'Liczba odwiedzin: {num_visit}')

    # Z tą wiedzą przechodzimy do systemu autoryzacji użytkownika.