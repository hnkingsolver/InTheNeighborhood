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

def books(request):
    return render(request, "books.html")

def beautyBrands(request):
    return render(request, "beauty_brands.html")

def donate(request):
    return render(request, "donate.html")

def localArtists(request):
    return render(request, "local_artists.html")

def restaurants(request):
    return render(request, "restaurants.html")
