from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login


# passowrd for test user = catchmeifyoucan2222

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request,'index.html')

def loginUser(request):
    print('amsa') 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("asd",username,password) 
        

        user = authenticate(username=username, password=password)
     
        if user is not None:
             login(request,user)
             return redirect("/")
    
        else:
             return render(request,'login.html')
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")