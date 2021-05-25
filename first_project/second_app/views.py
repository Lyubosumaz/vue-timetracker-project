from django.shortcuts import render
from second_app.models import User

# Create your views here.


def index(request):
    context = {
        'insert_me': 'Now I am coming from second_app/index.html',
    }
    return render(request, 'second_app/index.html', context)


def users(request):
    context = {
        'users': User.objects.order_by('first_name'),
    }
    return render(request, 'second_app/users.html', context)
