from django.shortcuts import render, HttpResponse, redirect, render



def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def resources(request):
    return render(request, "resources.html")

