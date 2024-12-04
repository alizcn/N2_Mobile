from django.db import models

# Create your models here.
class Geo(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    
class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE, null=True)

class Company(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)    
    phone = models.CharField(max_length=20)
    website = models.URLField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnail_url = models.URLField()

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)