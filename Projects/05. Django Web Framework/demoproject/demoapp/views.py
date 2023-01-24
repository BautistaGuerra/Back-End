from django.shortcuts import render

from django.http import HttpResponse
from demoapp.forms import InputForm

def index(request):
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def home(request):
    return HttpResponse("Welcome!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")

def form_view(request):
    form = InputForm()
    context = {"form": form}
    render(request, "home.html", context)