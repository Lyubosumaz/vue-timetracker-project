from django.shortcuts import render
from first_app.models import AccessRecord
from first_app.forms import FormName, UserForm, UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def index(request):
    context = {
        'access_records': AccessRecord.objects.order_by('date'),
        'insert_me': 'now i am coming from',
        'insert_me_too': 'first_app/index.html',
        'number': '1',
    }
    return render(request, 'first_app/index.html', context)


def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

    # if form.is_valid():

    return render(request, 'first_app/formname.html', {'formname': form})


def base(request):
    return render(request, 'first_app/base.html')


def other(request):
    return render(request, 'first_app/other.html')


def retrieve_url_templates(request):
    return render(request, 'first_app/retrieve_url_templates.html')


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'first_app/registration.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/other/')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")
