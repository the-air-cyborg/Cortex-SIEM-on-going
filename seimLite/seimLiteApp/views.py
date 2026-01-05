from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Log


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "seimLiteApp/login.html", {"form": form})


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
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "seimLiteApp/dashboard.html")


@login_required
def logs_view(request):
    logs = Log.objects.all()

    level = request.GET.get("level")
    status = request.GET.get("status")
    source = request.GET.get("source")

    if level:
        logs = logs.filter(level=level)

    if status:
        logs = logs.filter(status=status)

    if source:
        logs = logs.filter(source__icontains=source)

    logs = logs.order_by("-timestamp")

    return render(request, "seimLiteApp/logs.html", {
        "logs": logs,
        "selected_level": level,
        "selected_status": status,
    })
