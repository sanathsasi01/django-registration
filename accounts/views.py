from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.


def registration(request):
    return render(request, 'accounts/registration.html')
# user registration
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password1)
                print('user created')
                return redirect('registration')
        else:
            return HttpResponse(form.errors.as_text())

# user login
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_staff:
            print('true')
            login(request, user)         
            return redirect('adminPage')
        else:
            login(request, user)
            request.session['username'] = username
            return redirect('userPage')
    else:
        messages.info(request, 'Invalid Credentials')
        return redirect('registration')


# home page
# def homePage(request):
#     products = Products.objects.all()
#     context = {
#         'products':products
#     }
#     return render(request,'home.html',context)



# user logout
def logout_view(request):
    # del request.session['username']
    logout(request)
    return redirect('registration')