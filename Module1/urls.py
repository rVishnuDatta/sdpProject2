from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Hello/', hello1),
    path('hello1/',hello,name='hello'),
    path('',NewHomePage,name='NewHomePage'),
    path('Travel/',TravelPackage,name='TravelPackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('random/',random123, name='random123'),
    path('rand/',rand,name='rand'),
    path('get_date/',get_date,name='get_date'),
    path('getdate/',getdate1,name='getdate1'),
    #path('time/', tzfunctioncall, name='tzfunctioncall'),
    path('reg/', register1, name='register1'),
    path('reg1/', registerloginfunction, name='registerloginfunction'),
    path('pie1/',pie_chart1,name='pie1'),
    path('pie/',pie_chart,name='pie'),
    path('slides/',slides,name='slides'),
    path('w/',weatherlogic,name='weatherlogic'),
    path('weather/',weatherpagecall , name='weatherpagecall'),
    path('login/',login, name = 'login'),
    path('signup/',signup, name='signup'),
    path('signup1/',signup1, name='signup1'),
    path('login1',login1, name='login1'),
    path('logout/',logout, name='logout'),
]
