from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Now I am coming from second_app/index.html'}
    return render(request, 'second_app/index.html', context=my_dict)
