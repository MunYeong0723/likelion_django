from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'])
            auth.login(request, user) # login
            return render(request, 'index.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pw = request.POST['password']
        user = auth.authenticate(request, username=email, password=pw)
        if user is not None:
          auth.login(request, user)
          return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
