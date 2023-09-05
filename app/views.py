from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Profile, Courses
from .forms import RegistrationForm
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
# def home(request):
#     return HttpResponse("welcome")
def home(request):
    return render(request, "home.html");


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if user.check_password(password):
                auth.login(request, user)  # Correct order of arguments
                return redirect("dashboard")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


@login_required
def dashboard(request):
    user = request.user
    user_data = User.objects.get(id=user.id)
    print(user_data)
    print(user.id)
    profile_data = Profile.objects.get(user_id=user.id)
    return render(request, "dashboard.html", {"userDetails": user_data, "profileData": profile_data})


def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return redirect("registration")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=firstname,
                    last_name=lastname
                )
                subject = "Welcome to Vintage Info Solutions"
                message = f"Hai {user.first_name, user.last_name}, Thank you for registering in Vintage Info Solutions"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                details = Profile()
                details.user = user
                details.gender = request.POST["radio"]
                details.date = request.POST["date"]
                details.district = request.POST["hai"]
                details.state = request.POST["hello"]
                details.country = request.POST["country"]
                details.pin = request.POST["pin"]
                details.upload_image = request.FILES["file"]
                details.save()
                return redirect("login")
        else:
            return redirect("registration")
    else:
        return render(request, "registration.html")


def course_new(request):
    details=Courses.objects.all()
    return render(request, "course_new.html",{"Courses":details})
