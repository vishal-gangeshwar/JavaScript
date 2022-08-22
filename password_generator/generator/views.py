from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')





def password(request):

    thepassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):           # if you want to have capital letters included in the password
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):           # if you want to have capital letters included in the password
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'):           # if you want to have capital letters included in the password
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)



    return render(request, 'generator/password.html', {'password': thepassword})
