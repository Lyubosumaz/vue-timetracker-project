from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formname/', views.form_name_view, name='form_name')
]
