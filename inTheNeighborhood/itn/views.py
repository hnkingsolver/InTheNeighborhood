from django.shortcuts import render, HttpResponse, redirect, render

#just to see server
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def resources(request):
    return render(request, "resources.html")

def articles(request):
    return render(request, "articles.html")