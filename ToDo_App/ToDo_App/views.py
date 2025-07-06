# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False)
    contexts = {
        'tasks':tasks
    }
    return render(request, "home.html", contexts)