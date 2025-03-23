from rest_framework import serializers
from .models import User, Book
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod                                  # decorator that does not operates on instance of the class but operates on class itself
    def get_token(cls, user):                     # classmethod always takes "cls" as first parameter instead of self
        token = super().get_token(user)           # for getting JWT token
        token['email'] = user.email               # stores user email in token
        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        if email and password:
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                return super().validate(attrs)
        
        raise serializers.ValidationError("Invalid credentials")

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password']    # This Fields will be included
        extra_kwargs = {'password':{'write_only' : True}}   # prevents password from being expossed

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 