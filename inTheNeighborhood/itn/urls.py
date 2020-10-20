from django.urls import path

from .import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('resources', views.resources),
    path('books-articles', views.books),
    path('beauty-brands', views.beautyBrands),
    path('donate', views.donate),
    path('local-artists', views.localArtists),
    path('restaurants', views.restaurants),
    path('products-services', views.products_services),
    path('contact-us', views.contact_us),
    path('create-contact', views.create_contact),
    path('contacts-page', views.contacts_page),    
]

#archived urls incase we want them in the future
    # path('new-artist', views.new_artist),
    # path('new-restaurant', views.new_restaurant),
    # path('new-beauty', views.new_beauty),
    # path('new-article', views.new_article),
    # path('new-book', views.new_book),
    # path('create-artist', views.create_artist),
    # path('create-restaurant', views.create_restaurant),
    # path('create-beauty', views.create_beauty),
    # path('create-book', views.create_book),
    # path('create-article', views.create_article),
    # path('create-product', views.create_product),
    # path('create-service', views.create_service),