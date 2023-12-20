from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sold_by')
    sold_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sold_to')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(null=True)
    name = models.CharField(max_length=30, null=True)
    language = models.CharField(max_length=30, null=True)
    format = models.CharField(max_length=30, null=True)
    publisher = models.CharField(max_length=30, null=True)
    edition = models.CharField(max_length=30, null=True)
    pages = models.CharField(max_length=30, null=True)
    author = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    status =  models.CharField(max_length=30, null=True, default="Available")
    condition = models.CharField(max_length=30, null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.category.name+"--"+self.name

class Status(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    quantity = models.CharField(max_length=100, null=True)
    total = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.profile.user.username + " . " + self.product.name


class Booking(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    booking_id = models.CharField(max_length=200,null=True)
    quantity = models.CharField(max_length=100,null=True)
    book_date = models.CharField(max_length=30, null=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.book_date+" "+self.profile.user.username



class Send_Feedback(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.profile.user.username


class Make_Template(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    audio = models.FileField(null=True, blank=True)
    person1 = models.FileField(null=True, blank=True)
    person2 = models.FileField(null=True, blank=True)
    heart_image = models.FileField(null=True, blank=True)
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.profile.user.username


