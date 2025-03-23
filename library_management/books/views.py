from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Book, User
from .serializers import UserSerializer, BookSerializer, MyTokenObtainPairSerializer

class AdminSignupView(generics.CreateAPIView):  #for admin to signup
    queryset = User.objects.all()   
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]     # user can access without any restriction

class BookListCreateView(generics.ListCreateAPIView):   # for creating the book
    queryset = Book.objects.all()   
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # can only access with the user is authenticated

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):    # For update(put/patch) and delete
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = [permissions.IsAuthenticated]

class StudentBookListView(generics.ListAPIView):    # Students View to list book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


def book_list_view(request):    # Template View for listing books
    books = Book.objects.all()  # selecting all the books in the Book table
    return render(request, 'books/book_list.html', {'books':books})     # Rendering html template which will have Read_access to Book table in the database
