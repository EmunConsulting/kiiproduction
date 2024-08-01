from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from decorators import unauthenticated_user, allowed_users, authentication_required
from django.contrib.auth.decorators import login_required
from . models import UserRecord, ProfileImage


@login_required(login_url='login')
def home(request):
    # Check if the welcome message has already been displayed
    if not request.session.get('welcome_message_displayed', False) and request.user.is_authenticated:
        messages.success(request, str(request.user) + " " + ("logged in"))

        # Set the session variable to True to indicate that the welcome message has been displayed
        request.session['welcome_message_displayed'] = True

    return render(request, 'home.html', {})


def access_denied(request):
    return render(request, 'access_denied.html', {})


@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Assign user to the "traveler" group
                traveler_group, created = Group.objects.get_or_create(name='newUser')
                user.groups.add(traveler_group)

                messages.success(request, "Registration Successful")
                return redirect('home')  # Redirect to the page to add traveler details
    else:
        form = RegistrationForm()
    return render(request, 'register_user.html', {'form': form})


@authentication_required
def add_user_record(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        whatsapp_number = request.POST['whatsapp_number']
        email = request.POST['email']

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        new_rec = UserRecord(
            user=user,  # Linking UserRecord to the authenticated user
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone_number=phone_number,
            whatsapp_number=whatsapp_number,
            email=email,
        )
        new_rec.save()

        messages.success(request, "Record Added")
        return redirect('upload_profile_image')
    else:
        return render(request, 'user_record.html', {'user_email': request.user.email})


def upload_profile_image(request):
    if request.method == 'POST':
        print("POST request received")  # Debugging line
        if 'profile_image' in request.FILES:
            print("File received")  # Debugging line
            profile_image_file = request.FILES['profile_image']
            profile_image, created = ProfileImage.objects.get_or_create(user=request.user)
            profile_image.profile_image = profile_image_file
            profile_image.save()
            print(f"Profile image saved: {profile_image.profile_image.url}")  # Debugging line
            return redirect('home')  # Replace 'home' with the name of the view you want to redirect to
        else:
            print("No file received")  # Debugging line
    else:
        print("Not a POST request")  # Debugging line
    return render(request, 'upload_profile_image.html')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Wrong User Name or Password"))
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logout completed"))
    return redirect('home')


@authentication_required
def profile_view(request):

    try:
        profile_image = ProfileImage.objects.get(user=request.user)
    except ProfileImage.DoesNotExist:
        profile_image = None

    context = {
        'profile_image': profile_image,
    }

    return render(request, 'navbar.html', context)
