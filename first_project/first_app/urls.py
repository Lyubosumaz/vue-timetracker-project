from django.urls import path
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('formname/', views.form_name_view, name='form_name'),
    path('base/', views.base, name='base'),
    path('other/', views.other, name='other'),
    path('retrive/', views.retrive_url_template, name='retrive_url_template'),
]
