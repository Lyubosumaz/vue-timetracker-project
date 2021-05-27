from django.shortcuts import render
from second_app.models import User
# TODO SHOULD BE .forms
from second_app.form import NewUserForm
# Create your views here.


def index(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('ERROR FORM INVALID')

    context = {
        'insert_me_text': 'Go to /users to sign up!',
        'insert_me_message': 'Please sing up here!',
        'form': form,
    }
    return render(request, 'second_app/index.html', context)


def users(request):
    context = {
        'users': User.objects.order_by('first_name'),
    }
    return render(request, 'second_app/users.html', context)
