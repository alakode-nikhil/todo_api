from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='reg_user'),
    path('login/', UserLoginView.as_view(), name='login_user'),
]