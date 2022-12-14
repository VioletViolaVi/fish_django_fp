from ast import Pass
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # this part creates the user
            # can't use this until validated
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"User '{username}' successfully created")
            return redirect("animals-home")
    else:
        form = UserRegistrationForm()

    data = {"form": form}
    return render(request, "register.html", data)
