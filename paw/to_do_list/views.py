from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.models import User
from .models import Task
from .filter import Orderfilter

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
 
    tasks = Task.objects.filter(username=request.user.username)
    myfilter =  Orderfilter(request.GET , queryset = tasks)
    tasks = myfilter.qs
    return render(request , "to_do_list/home.html" , {
        "tasks" : tasks , 'myfilter' : myfilter
    } )
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username = username , password = password)
        if user is not None :
            login(request ,user)
            return HttpResponseRedirect(reverse("index"))
        else : 
            return render(request , "to_do_list/login.html" , {
                "message" : "invaled credentials."
            })
    return render(request , "to_do_list/login.html" )

def logout_view(request):
    logout(request)
    return render(request , "to_do_list/login.html" , {
        "message" : "Logged out"
    })
def signin(request):
    if request.method == "POST" :
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password1"]
        pass2 = request.POST["password2"]
        #create user
        myuser = User.objects.create_user(username , email , pass1)
        myuser.save()
   
    return render(request , 'to_do_list/signin.html')
    
def add(request):
    if request.method == 'POST':
        tasks = Task()
        tasks.username = request.user.username
        tasks.email = request.user.email
        tasks.task = request.POST["task"]
        tasks.time = request.POST["time"]
        tasks.notify = request.POST["notify"]
        tasks.save()        

    return HttpResponseRedirect(reverse("index"))

def delete(request ,id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return HttpResponseRedirect(reverse("index"))