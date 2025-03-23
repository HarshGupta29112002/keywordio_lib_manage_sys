from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AdminSignupView, BookListCreateView, BookDetailView, StudentBookListView, book_list_view
from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):       # Generates referesh and access token
    serializer_class = MyTokenObtainPairSerializer      # using custom serializer


urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    # path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('student/books/', StudentBookListView.as_view(), name='student-book-list'),
    path('books/template/', book_list_view, name='book-list-template'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
