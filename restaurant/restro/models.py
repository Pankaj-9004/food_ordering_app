from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    mobile = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Meal(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='Meal')
    price = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.name)


class Order(models.Model):
    choices = (('Received', 'Received'),
               ('Scheduled', 'Scheduled'),
               ('Shipped', 'Shipped'),
               ('In Progress', 'In Progress'),
              )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="media", null=True)
    meal = models.CharField(max_length=1000, null=True)
    quantity = models.CharField(max_length=5, null=True, blank=True)
    price = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    address = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=13, null=True)
    zipcode = models.CharField(max_length=6, null=True)
    status = models.CharField(max_length=500, choices=choices, default="In Progress")
    deliver_date = models.DateTimeField(auto_now_add=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.meal)

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    message = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)