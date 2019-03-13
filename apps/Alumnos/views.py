from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Test</h1><h2>otro test</h2>")
