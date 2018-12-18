from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.conf import settings

def Contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
            email = form.cleaned_data.get("email")
            full_name = form.cleaned_data.get("full_name")
            message = form.cleaned_data.get("message")
            subject = "Müşteri Formu"
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email, "tercuman4848@gmail.com"]
            contact_message = "%s: %s via %s"%(
                email,
                full_name,
                message)
            send_mail(subject,
            contact_message, 
            from_email, 
            to_email,
            fail_silently=True )
            
            messages.success(request,"İsteğiniz Bize İletildi.Daha Hızlı Ulaşmak İçin 0 555 966 70 92 Numaradan Bizlere Ulaşa Bilirsiniz ...")
       

            return redirect("index")    


            
                


    context ={
            "form" :form
        }
    return render(request,"contact.html",context)   


def Flamenco(request):
    return render(request,"flameco.html")


def Almanca(request):
    return render(request,"almanca.html")    

def England(request):
    return render(request,"england.html")

def net(request):
    return render(request,"net.html")





