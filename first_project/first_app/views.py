from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage


def index(request):
    context = {
        'access_records': AccessRecord.objects.order_by('date'),
        'insert_me': 'Now I am coming from first_app/index.html'
    }
    return render(request, 'first_app/index.html', context)
