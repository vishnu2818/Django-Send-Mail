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
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    # Getting the logged-in user (request.user)
    user = request.user
    try:
        if request.method == 'POST':
            # email = request.method.POST['email']
            # subject = request.method.POST['subject']
            # message = request.method.POST['message']
            message = request.POST.get('message', '').strip()
            subject = request.POST.get('subject', '').strip()
            email = request.POST.get('email', '').strip()

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # From email (configured in settings.py)
                [email],  # To email (from the form)
                fail_silently=False,
            )

            # If successful, send a success message
            messages.success(request, 'Your message has been sent!')

    except Exception as e:
        # General exception handler if anything unexpected occurs
        messages.error(request, f'There was an error sending your message: {str(e)}')

    # Querying Users
    users = User.objects.all()
    for user in users:
        print(user.username)
        print(user.email)
    return render(request, 'home.html', {'user': user})