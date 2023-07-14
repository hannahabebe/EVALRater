from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
  return render(request, 'performance/index.html')

def menu(request):
  return render(request, 'performance/menu.html')

def dashboard(request):
  return render(request, 'performance/dashboard.html')

def department(request):
  return render(request, 'performance/department.html')

def employee(request):
  return render(request, 'performance/employee.html')

def training(request):
  return render(request, 'performance/training.html')

def development(request):
  return render(request, 'performance/development.html')

def panel(request):
  return render(request, 'performance/adminPanel.html')

# def order(request):
#   return render(request, 'performance/order.html')

# def file(request):
#   return render(request, 'performance/file.html')