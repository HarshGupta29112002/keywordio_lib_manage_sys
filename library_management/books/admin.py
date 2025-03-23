from django.contrib import admin
from .models import Book, User

# Register your models here.

admin.site.register(User)   # using this So that the User table to be registered on admin panel
admin.site.register(Book)