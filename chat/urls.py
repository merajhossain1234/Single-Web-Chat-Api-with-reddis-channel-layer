from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_registration'), 
    path('login/', Login.as_view(), name='user_login'), 
]