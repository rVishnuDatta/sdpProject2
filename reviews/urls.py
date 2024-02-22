from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from . import views
from .views import *
from django.conf import settings

urlpatterns = [
    path('',review_list, name='review_list'),
    path('add/',add_review, name='add_review'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
