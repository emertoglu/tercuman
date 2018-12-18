from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm  #oluşturulan formlar buraya giriliyor.

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from django.contrib.auth import login,authenticate,logout
from django.contrib import messages





def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")   
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        
        

        user = User(username =username , email=email , first_name = first_name, last_name = last_name)
        user.set_password(password)

        user.save()
        login(request,user)
        messages.success(request,"Tebrikler Giriş Yaptınız")
       

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context) 

   
   
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı") 
    return redirect ("index")

def Contact(request):
    return render(request,"contact.html")






