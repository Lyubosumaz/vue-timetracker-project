from django.shortcuts import render
from first_app.models import AccessRecord
from first_app.forms import FormName


def index(request):
    context = {
        'access_records': AccessRecord.objects.order_by('date'),
        'insert_me': 'Now I am coming from first_app/index.html'
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