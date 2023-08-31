from django.shortcuts import render

tasks=['f', 'd', 'sd']
# Create your views here.
def index(request):
    render(request, "tasks/index.html", {
        "tasks":tasks
    })