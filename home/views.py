from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoCreateFrom
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    object_list = Todo.objects.all()
    paginator = Paginator(object_list,1)  # در هر صفحه 3 پست نمایش بده
    page = request.GET.get('page')  # استفاده میکنیم GET طبق داکیومنت جنگو، برای گرفتن شماره صفحه، از
    try:
        todo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        todo = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        todo = paginator.page(paginator.num_pages)

    return render(request , 'home.html' , {'todos' : todo})

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
