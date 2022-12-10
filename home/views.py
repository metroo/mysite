from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoCreateFrom
from django.contrib import messages

# Create your views here.

def home(request):
    all = Todo.objects.all()
    return render(request , 'home.html' , {'todos' : all})

def detail(request , todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render(request , 'detail.html',{'todo' :todo})

def delete(request , todo_id):
    todo = Todo.objects.get(id=todo_id).delete()
    messages.success(request , 'deleted Successfully' , extra_tags='primary')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = TodoCreateFrom(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'] ,body=cd['body'], created=cd['created'])
            messages.success(request , 'Todo add' , 'success')
            return redirect('home')
    else :
        form = TodoCreateFrom()
    return render(request , 'create.html' , {'form': form})
