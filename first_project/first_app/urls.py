from django.urls import path
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('formname/', views.form_name_view, name='form_name'),
    path('base/', views.base, name='base'),
    path('other/', views.other, name='other'),
    path('retrive/', views.retrieve_url_templates, name='retrieve_url_templates'),
    path('register/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='login'),
]
