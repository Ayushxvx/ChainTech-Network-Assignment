from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import CustomUser
# Create your views here.
def index(request):
    response = requests.get("https://programming-quotesapi.vercel.app/api/random")
    if response.status_code == 200:
        randQuote = response.json()["quote"]
        author = response.json()["author"]
        return render(request,"a/index.html",{"randomQuote":randQuote,"author":author})
    else:
        print("not able to get quote")
        return render(request,"a/index.html",{})

def anything(request,anything):
    content = f"<h1 style='text-align:center;padding:16px;'>{anything}</h1>"
    return HttpResponse(content)

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age  = request.POST.get("age")
        content = {
            "name":name,
            "email":email,
            "age":age
        }
        user = CustomUser(name=name,email=email,age=age)
        user.save()
        return render(request,"a/form.html",content)
    else:
        return render(request,"a/form.html",{})
    
def showUser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            userdata = CustomUser.objects.get(name=name)
            if userdata:
                return render(request,"a/showUser.html",{"userdata":userdata})
        except:
            return render(request,"a/showUser.html",{"message":"No user found with given name"})
    return render(request,"a/showUser.html",{})
