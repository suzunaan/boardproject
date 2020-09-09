from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def signupfunc(request):
    user2=User.objects.all()
    print(user2)
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            User.objects.get(username=username)
            return render(request,"signup.html",{"error":"このユーザーは登録されています"})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request,"signup.html",{"some":100})
    return render(request,"signup.html",{"some":100})

def loginfunc(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("signup") 
        else:
            return redirect("login")
    return render(request,"login.html")

def listfunc(request):
    return render(request,"list.html")
