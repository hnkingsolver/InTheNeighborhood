from django.db import models
import re

class ResourceManager(models.Manager):
    def create_validator(self,requestPOST):
        errors = {}
        if len(requestPOST['name']) < 2:
            errors['short_name'] = "Name must be at least 2 characters"
        existing_artist = Artist.objects.filter(name=requestPOST['name'])
        existing_restaurant = Restaurant.objects.filter(name=requestPOST['name'])
        existing_beauty = BeautyBrand.objects.filter(name=requestPOST['name'])
        if len(existing_artist) > 0 or len(existing_restaurant) > 0 or len(existing_beauty) > 0:
            errors['duplicate_resource'] = "This resource already exists in our database"
        return errors

class BookManager(models.Manager):
    def create_validator(self,requestPOST):
        errors = {}
        if len(requestPOST['title']) < 2:
            errors['short_title'] = "Title must be at least 2 characters"
        existing_book = Book.objects.filter(title=requestPOST['title'])
        if len(existing_book) > 0 > 0:
            errors['duplicate_resource'] = "This book already exists in our database"
        return errors
    
class ArticleManager(models.Manager):
    def create_validator(self,requestPOST):
        errors = {}
        if len(requestPOST['title']) < 2:
            errors['short_title'] = "Title must be at least 2 characters"
        existing_article = Book.objects.filter(title=requestPOST['title'])
        if len(existing_article) > 0 > 0:
            errors['duplicate_resource'] = "This article already exists in our database"
        return errors
    
class ContactManager(models.Manager):
    def create_validator(self,requestPOST):
        errors = {}
        if len(requestPOST['name']) < 2:
            errors['name'] = "First name is too short."
        if len(requestPOST['email']) < 6:
            errors['email'] = "Email is too short"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestPOST['email']) > 0:
            if not EMAIL_REGEX.match(requestPOST['email']):
                errors['email_format'] = "Email is not in correct format"
        return errors
    

class Artist(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()

class BeautyBrand(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    publisher = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    
class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ArticleManager()

class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()

class Service(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()

class FashionBrand(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ResourceManager()
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ContactManager()