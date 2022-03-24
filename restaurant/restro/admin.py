from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Contact)