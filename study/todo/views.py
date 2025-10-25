from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo
from django.template import loader

from .forms import RegisterForm
from .models import Users

def main(request, firstname):
    tasks = Todo.objects.filter(firstname=firstname)
    form = TodoForm()
    context = {
    'alltasks': tasks,
    'form': form,
     }
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.firstname = firstname
            new_task.lastname = "pohui"
            new_task.save()
            form = TodoForm()
            context['form'] = form
            return render(request, 'main.html',  context)
            
    return render(request, 'main.html',  context)

def register(request):
    form = RegisterForm()
    context = {
    'form': form,
     }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            is_name_exists = Users.objects.filter(firstname=firstname).exists()
            if is_name_exists:
                return redirect(f"/main/{firstname}")
            else:
                form.save()
                return HttpResponse("You are saved")
            
    return render(request, 'register.html',  context)

def testing(request):
  template = loader.get_template('testing.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def deletetask(request, id, firstname):
    task = Todo.objects.filter(id=id)
    task.delete()
    return redirect(f"/main/{firstname}")


