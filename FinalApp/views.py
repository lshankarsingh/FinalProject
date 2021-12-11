from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasklist
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
@login_required
# Create your views here.

def first(request):
    if(request.method=="POST"):
        form=TaskForm(request.POST or None)
        if(form.is_valid()):
            instance=form.save(commit=False)
            instance.owner=request.user
            #form.save(commit=False).owner=request.user
            instance.save()
        messages.success(request,("New Task Added"))
        return redirect('first') #Here first is the url specificin urls
    else:
        all_tasks=Tasklist.objects.all()
        paginator=Paginator(all_tasks,10) #creating object of paginator class
        page=request.GET.get('page') #Here To get a particular page
        # Now reloading all_tasks as per our paginator results
        all_tasks=paginator.get_page(page)
        return render(request,'base.html',{'all_tasks':all_tasks})

@login_required
def contact(request):
    context={
        'contact_text':'welcome to the Contact page'
    }
    return render(request,'contact.html',context)


def about(request):
    context={
        'about_text':'welcome to the About page'
    }
    return render(request,'about.html',context)

def index(request):
    context={
        'index_text':'welcome to the Index page'
    }
    return render(request,'index.html',context)
    
@login_required
def delete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.delete()
    return redirect('first')

@login_required
def edit_task(request,task_id):
    if(request.method=="POST"):
        task=Tasklist.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if(form.is_valid()):
            form.save()
        messages.success(request,("Task Edited"))
        return redirect('first') #Here first is the url specified urls
    else:
        task_obj=Tasklist.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

@login_required
def complete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('first')

@login_required
def pending_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('first')
