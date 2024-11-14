from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Volunteer
from .forms import VolunteerForm

# Create your views here.
def home_page(request):
    """Renders the home page if the user is authenticated, otherwise redirects to the login page.

    :param :request (HttpRequest): The HTTP request object.

    Returns: HttpResponse: The rendered home page or a redirect to the login page.

    :rtype: HTTP object
    """
    if request.user.is_authenticated:
        return render(request, 'pages/home.html')
    else:
        return redirect('login')


def about_page(request):
    """Renders the about page.

    :param: request (HttpRequest): The HTTP request object.

    Returns: HttpResponse: The rendered HTML response.

    :rtype: HTTP object
    """
    return render(request, 'pages/about.html')


def authenticate_user(request):
    """
    Logs in a user based on POST data.

    - Retrieves username and password from POST data.
    - Authenticates with Django's `authenticate`.
    - Redirects to login on failure, shows user on success.
    
    Args:
        request (HttpRequest): The Django HTTP request object containing the POST data.

    Returns:
        HttpResponseRedirect: A redirect response object 
        directing the user to either the login page (on failure) or a specific page after success.
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('register'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    

def register_user(request):
    """
    Registers a new user on the system.

    Args:
        request (HttpRequest): The HTTP request object containing form data.

    Returns:
        HttpResponse:
            * An `HttpResponseRedirect` object redirecting to the login page (on successful registration).
            * An `HttpResponse` object rendering the registration form (on GET request or invalid form submission).
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.is_valid)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
        return render(request, 'pages/reg.html',{'form': form})

def user_login(request):
    """
    Handles user login requests.

    Args:
        request (HttpRequest): The Django request object.

    Returns:
        HttpResponse:
            - A redirect response to the home page if login is successful.
            - An HTTP response rendering the login form template for GET requests.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request,'pages/login.html', {'form': form})
    

def register_volunteer(request):
    """
    Registers a new volunteer based on the submitted form data.

    Args:
        request (HttpRequest): The Django HTTP request object containing form data
                             or indicating the HTTP method.

    Returns:
        HttpResponse:
            - A rendered template (`pages/volunteer.html`) with an empty form on GET requests.
            - A redirect response to the homepage (`'home'`) on successful POST requests.
            - A rendered template with the invalid form pre-populated on invalid POST requests.
    """
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VolunteerForm()
        return render(request, 'pages/volunteer.html', {'form': form})


def logout_view(request):
    """Logs out the current user and redirects to the login page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The response redirecting to the login page.
    """
    logout(request)
    return redirect('login') 