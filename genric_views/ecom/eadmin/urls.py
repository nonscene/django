from django.urls import path
from .views import *

url_patterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(),name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]