from django.shortcuts import render
from django import forms
tasks=['f', 'd', 'sd']
# Create your views here.
class newTaskForm(forms.Form):
    task=forms.CharField(label="new task")
    priority=forms.IntegerField(label="Priority", min_value=1, max_value=7)
def index(request):
    return render(request, "tasks/index.html", {
        "tasks":tasks
    })
def add(request):
    if request.method=="POST":
        form=newTaskForm(request.POST)
        if form.is_valid:
            task=form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form":form
            })
    return render(request, "tasks/add.html", {
        "form":newTaskForm()
    })