from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from todolist.models import Todolist

def index(response):
    return HttpResponse("index")

def usr(response, username):
    todolist = Todolist.objects.all().filter(usrname=username)

    return render(response, 'todolist/todolist.html', {'todolist':todolist})

def delete(response, bid):

    job = Todolist.objects.get(id=bid)
    name = job.usrname
    if job:
        job.delete()
    ulr = '/' + name
    return redirect(ulr)

def complete(response, bid):

    job = Todolist.objects.get(id=bid)

    if job:
        job.is_complete = True
        job.save()
    name = job.usrname
    ulr = '/' + name
    return redirect(ulr)

def addnewjob(response):
    return render(response, 'todolist/Addnewjob.html')

def add_job(request):
    username = request.GET.get("username")
    tittle = request.GET.get("tittle")
    description = request.GET.get("description")
    job = Todolist()
    job.usrname = username
    job.tittle = tittle
    job.description = description
    job.save()
    ulr = '/' + username
    print(username+tittle+description)
    return redirect(ulr)
