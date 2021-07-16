from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout

# Create your views here.

def register(request):
        
        form = RegisterForm(request.POST or None)
        if form .is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            messages.success(request, 'Qeydiyyat uğurla tamamlandı.')

            return redirect("index")
        context = {
            "form":form
        }
        return render(request,"register.html",context)    
  
def loginuser(request):
   
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user =authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"İstifadəçi adı və ya şifrə yalnışdır.") 
            return render(request,"login.html",context)
        
        messages.success(request,"Giriş uğurla baş verdi")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)    

def logoutuser(request):
    logout(request)
    messages.success(request,"Sistemdən uğurla çıxıldı.")
    return redirect("index")
