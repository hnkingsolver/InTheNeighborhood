from django.shortcuts import render, HttpResponse, redirect, render

# Create your views here.
from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")
