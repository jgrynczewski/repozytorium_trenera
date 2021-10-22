from django.shortcuts import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, world")


def hello2(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>Hello, world</title></head><body><h2>Witaj, świecie</h2></body></html>")


def hello3(request):
    return render(request, 'templates/hello.html')