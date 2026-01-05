from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "seimLiteApp/login.html", {
        "form": form
    })

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "seimLiteApp/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request,'seimLiteApp/dashboard.html')

def logs_view(request):
    return render(request,'seimLiteapp/logs.html')

@login_required
def logs_view(request):
    dummy_logs = [
        {
            "time": "2026-01-03 11:30",
            "level": "INFO",
            "source": "Auth",
            "message": "User admin logged in",
            "status": "OK"
        },
        {
            "time": "2026-01-03 11:28",
            "level": "WARNING",
            "source": "Firewall",
            "message": "Multiple failed login attempts",
            "status": "Investigate"
        },
        {
            "time": "2026-01-03 11:25",
            "level": "CRITICAL",
            "source": "Server",
            "message": "Unauthorized access detected",
            "status": "Blocked"
        }
    ]

    context = {
        "logs": dummy_logs
    }

    return render(request, "seimLiteApp/logs.html", context)