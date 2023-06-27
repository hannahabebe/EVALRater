from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_page(request):
    if request.method == "POST":
        id = request.POST['employee_id']
        password = request.POST['password']
        user = authenticate(request, id=id, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, ("Invalid Id or password, Try Again!"))
            return redirect('login')
          
    else:
        return render(request, 'employee/login.html', {})