import random
import string


from django.http import HttpResponse
from .forms import *


# Create your views here.

def hello(request):
    return render(request, 'hello123.html')


def hello1(request):
    return HttpResponse("<center>Welcome to TTM HomePage</center>")


def NewHomePage(request):
    return render(request, 'NewHomePage.html')


def TravelPackage(request):
    return render(request, 'TravelPackage.html')


def print1(request):
    return render(request, 'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['vishnu']
        print(f'User input: {user_input}')
    # return HttpResponse('Form Submitt ed Successfully')
    a1 = {'user_input': user_input}
    return render(request, 'print_to_console.html', a1)


def rand(request):
    return render(request, 'random123.html')


def random123(request):
    if request.method == "POST":
        input1 = request.POST['input']
        input2 = int(input1)
        ran1 = "".join(random.sample(string.digits, input2))
        print(ran1)
        a2 = {'ran1': ran1}
        return render(request, 'random123.html', a2)


def getdate1(request):
    return render(request, 'get_date.html')


import datetime
from django.shortcuts import render


def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html', {'form': form})


'''def tzfunctioncall(request):
    return render(request, 'pytzexample.html')'''


def register1(request):
    return render(request, 'Register.html')


from .models import *
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1 = "Email already registered. Choose a different email"
            return render(request, 'Register.html', {'message1': message1})
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('NewHomePage')
    return render(request, 'Register.html')


def pie_chart1(request):
    return render(request, 'Piechart.html')


import matplotlib.pyplot as plt
import numpy as np


def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1 = {'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'PieChart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'PieChart.html', {'form': form})


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

def slides(request):
    return render(request,'Slides.html')

def weatherpagecall(request):
    return render(request , 'weatherappinput.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '23c7299db81788258802e020766fb76c'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request ,'login.html')
def signup(request):
    return render(request ,'signup.html')
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHomePage.html')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')

def signup1(request):
    if request.method=="POST":
        username= request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfullyy!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'password do not match')
            return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request, 'NewHomePage.html')