from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import AccountForm
from .models import Account
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"index.html")


def Translate(request):
    return render(request,"translate.html")
   



# Create your views here.
