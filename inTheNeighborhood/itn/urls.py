from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('resources', views.resources),
    path('articles', views.articles),
    path('books', views.books),
    
    path('beauty-brands', views.beautyBrands),
    path('donate', views.donate),
    path('local-artists', views.localArtists),
    path('restaurants', views.restaurants),
]