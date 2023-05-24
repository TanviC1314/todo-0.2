from socket import fromshare
from django import forms
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse

from .models import Todo


class MyForm(forms.Form):
    title =  forms.CharField(max_length=10, min_length=4)

def create(request):
    
    form_data= MyForm(request.POST)
    if(form_data.is_valid()):
        title = request.POST["title"]
        Todo.objects.create(title=title, is_completed=True)
        return redirect("index")
    else:
        return HttpResponse("Error Found")

def index(request):
    todos = Todo.objects.all()
    return render(request, "todo/index.html" , {
        "todos": todos,
        "form":MyForm()
    })

def toggle(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect("index")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")