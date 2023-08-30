from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app1/index.html")
def sandro(request):
    return HttpResponse("hi Sandro")
def marianne(request):
    return HttpResponse("So Long Marianne")

def greet(request, name):
    return HttpResponse(f"Hello,  {name.capitalize()}")

