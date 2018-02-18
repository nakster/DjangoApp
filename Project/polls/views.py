from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo
# Create your views here.
def index(request):
    todos = todo.objects.all()[:10]

    context = {
        'todos':todos,
    }
    return render(request, 'index.html', context)

def details(request, id):
    todos = todo.objects.get(id=id)

    context = {
        'todos':todos
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todos = todo(title=title, text=text)
        todos.save()

        return redirect('/polls')
    
    else:
        return render(request, 'add.html')
