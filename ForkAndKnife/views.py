from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm

from .models import Menu
# Create your views here.

def index(request):
    menus = Menu.objects.all()
    return render(request, "ForkAndKnife/index.html", {'menuss': menus})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            error_message = 'Invalid username or password.'
            return render(request, "ForkAndKnife/signin.html", {'error_message': error_message})
    else:
        return render(request, 'ForkAndKnife/signin.html')
    #return render(request, "ForkAndKnife/signin.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'ForkAndKnife/joinnow.html', {'form': form})

    #return render(request, "ForkAndKnife/joinnow.html")

def logoutview(request):
    logout(request)
    return redirect('indexPage')

def home(request):
    menus = Menu.objects.all()

    return render(request, 'ForkAndKnife/home.html',{'menuss': menus})


def menu(request):
    return render(request, "ForkAndKnife/menu.html")

def about(request):
    return render(request, 'ForkAndKnife/about.html')

# def profile(request,username):
    # user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(User, user=user)
    # context = {'user': user, 'profile': profile}
    # return render(request, "ForkAndKnife/profile.html",context)

def profile(request):
    return render(request, 'ForkAndKnife/profile.html')


