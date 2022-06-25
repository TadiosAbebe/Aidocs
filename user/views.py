from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.views import all_projects, home

def signup(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1 != password2):
            messages.error(request, 
                           "password doesn't match")
            return redirect(home)
        if(User.objects.filter(username=user_name).exists()):
            messages.error(request, 
                           "username already taken! please used a unique username")
            return redirect(home)
        usr = User.objects.create_user(user_name, email, password1)
        usr.first_name = first_name
        usr.last_name = last_name
        usr.save()
        messages.success(request, usr.first_name +
                         ', your account has been sucessfully created')
        return redirect(home)
    return render(request, "index.html")


def signin(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        user = authenticate(username=user_name, password=password1)
        if user is not None:
            login(request, user)
            content = {
                'first_name': user.first_name,
            }
            return redirect(all_projects)
        else:
            messages.error(
                request, 'Unable to log you in contact the adminstrator')
            return redirect(home)
    return render(request, "index.html")


def signout(request):
    logout(request)
    messages.success(request, "Signed out successful")
    return redirect(home)
