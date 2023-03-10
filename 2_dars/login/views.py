from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import SignUpForm

def register_user(request):
    msg = None
    succes = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            msg = "User created succesfully"
            succes = True

            return redirect('/accounts/login/')

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form' : form, 'msg' : msg, 'succes' : succes})