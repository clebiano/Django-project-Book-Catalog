from django.urls import path
from django.contrib import admin
from .viewsets import (
    UserCreateViewSet,
)


app_name = 'account'

urlpatterns = [
    path('register/', UserCreateViewSet.as_view(), name='register'),
]