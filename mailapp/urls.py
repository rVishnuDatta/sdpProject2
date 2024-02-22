from django.contrib import admin
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.send_emails, name='send_emails'),
]
