from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.models import User,auth
from .models import Department,Semester,Subjects,Book,Data
# Create your views here.
#def department(request):
#    return render(request,'depart.html')

#def subjects(request):
#    return render(request,'subjects.html')

#def book(request):
#    return render(request,'books.html')

def sems(request):
    return render(request,'semester.html')

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)

def post_detail(request,id):
    instance = get_object_or_404(Data, id=id)
    
    context = {
        "title": instance.title, 
        "instance" : instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Data.objects.all()
    context = {
        "object_list" : queryset,
        "title": "List" 
    }
    return render(request, "posts.html", context)

def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")

def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")