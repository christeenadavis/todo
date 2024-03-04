from django.shortcuts import render
from . models import Task
from . forms import  TodoForm
from django.views.generic import ListView
from
fr
fr
from
from

from
# Create your views here.
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

def add(request):
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        task=Task(name=name,priority=priority)
        task.save()
    return render(request,'home.html')

def details(request):
    task=Task.objects.all()
    return render(request,'detail.html',{'task':task})
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is valid():
     f.save()
     return render('/')
    return render(request,'edit.html',{'f':f,'task':task})