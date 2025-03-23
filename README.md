# keywordio_library_management_system

I have made this library management system using Django REST Framework amd Mysql.

# Following are the commands and steps of implementation

    STEP-1 : CREATE & ACTIVATE VIRTUAL ENVIRONMENT ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        CMD-1 : python -m venv <your virtual name>

            example: python -m venv venv
                        so, here "venv" is the name of virtual environment and using this command you can create a Virtual environment for your project.
        
        CMD-2 : . venv/Scripts/activate
                    This command basically activate your virtual environment.

    STEP-2 : INSTALL DEPENDENCIES ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        CMD : pip install django djangorestframework mysqlclient djangorestframework-simplejwt

            This will install the following packages in your system : {
                        
                                                                        asgiref==3.8.1
                                                                        Django==5.1.7
                                                                        djangorestframework==3.15.2
                                                                        djangorestframework_simplejwt==5.5.0
                                                                        mysqlclient==2.2.7
                                                                        PyJWT==2.9.0
                                                                        sqlparse==0.5.3
                                                                        tzdata==2025.1
                                                                        
                                                                    }

            This packages will be saved in requirements.txt file with the help of following commands :

                CMD-1 : pip freeze > requirements.txt
                CMD-2 : pip install -r requirements.txt

    STEP-3 : CREATE DJANGO PROJECT AND APP ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Create a new Django Project

            CMD : django-admin startproject library_management

        # Create an app

            CMD : python manage.py startapp books
                    Here "books" is the name of app

    STEP-4 : CONFIGURE settings.py FILE

        # Add 'books', 'rest_framework', 'rest_framework_simplejwt' in INSTALLED_APPS below its existing code.
            
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'books',                         # Added
                'rest_framework',                # Added
                'rest_framework_simplejwt',      # Added
            ]

        # Rest Framework authentication settings.

            REST_FRAMEWORK = {
                'DEFAULT_AUTHENTICATION-CLASSES':(
                    'rest_framework_simplejwt.authentication.JWTAuthentication',
                ),
            }

        # Setting-up Mysql database with XAMPP

            1.> Create a new DB named "library_db" in your Mysql DB
            2.> Create User, password, and select host
            3.> Now configure Mysql DB in settings.py file

                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': 'library_db',
                        'USER': 'Harsh',
                        'PASSWORD': 'Harsh@123',
                        'HOST': 'localhost',
                        'PORT': '3306',
                    }
                }                

    STEP-5 : CREATE MODELS (models.py in books app). ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Create your models.

    STEP-6 : CREATE A NEW serializers.py FILE IN YOUR BOOKS APP ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Create your modelserializers.

    STEP-7 : CREATE VIEWS (views.py in books app) ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Create your views to perform CRUD operations here.

    STEP-8 : DEFINE URLs (urls.py in books app) ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Make sure to create your urlpatterns here.

    STEP-9 : CONFIGURE PROJECT URLs (urls.py in library_management) ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        # Make sure to write the following code with the existing code. 

        CODE :  
                1.> from django.urls import include
                2.> path('api/', include('books.urls')), 
    
    STEP-10 : RUN MIGRATIONS ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        CMD-1 : python manage.py makemigrations
        CMD-2 : python manage.py migrate

    STEP-11 : CREATE SUPERUSER ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        CMD : python manage.py createsuperuser

    STEP-12 : START SERVER ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        CMD : python manage.py runserver

# Reference: 

    1. Django - (https://docs.djangoproject.com/en/5.1/)

    2. Django_Rest_Framework - (https://www.django-rest-framework.org/)

    3. DjangoRestFramework_simpleJWT - (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
