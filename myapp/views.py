from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        print("Method Post!")
        # username = request.POST['username']
        # email = request.POST.get('email')
        email = request.POST['email']
        password = request.POST['password']
        print(email)

        # get the user object by email
        user = User.objects.get(email=email)
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            print("Logged in!")
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'index.html')

from django.contrib.auth.models import User

def home(request):
    # Getting the logged-in user (request.user)
    user = request.user

    # Check if the user is authenticated
    if user.is_authenticated:
        print(user.username,"hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")  # Print username to console
        print(user.email)  # Print email to console

    # Querying Users
    users = User.objects.all()
    for user in users:
        print(user.username)
        print(user.email)
    return render(request, 'home.html', {'user': user})