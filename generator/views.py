from django.shortcuts import render
import random


# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('specials'):
        characters.extend(list('!#$%&()¿?@+-*_'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for _ in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})
