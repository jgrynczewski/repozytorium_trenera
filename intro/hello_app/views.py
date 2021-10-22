import datetime

from django.shortcuts import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>ABC</title></head><body><h2>Hello, world!</h2></body></html>")


def hello2(request):
    return render(request, 'hello_app/hello.html')


def adam(request):
    return HttpResponse("Hello, Adam")


def ewa(request):
    return HttpResponse("Hello, ewa")


def name(request, name):
    return HttpResponse(f"Hello, {name}")


def name2(request, name):
    name = name.title()
    return render(request, "hello_app/hello2.html", {"name" : name})


def new_year(request):
    now = datetime.datetime.now()
    is_new_year = True if (now.day == 1 and now.month == 1) else False

    return render(
        request,
        'hello_app/isitnewyear.html',
        {"is_new_year": is_new_year}
    )