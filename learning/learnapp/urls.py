from django.contrib import admin
from django.urls import path, include
from learnapp import views

app_name='learnapp'

urlpatterns=[
path('register/',views.register,name='register')
]
