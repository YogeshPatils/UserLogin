from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',userSignUpView),
    path('login/',userLogInView),
    path('uservalidate/',userNameValidateView)
]