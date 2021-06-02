from django.urls import path
from index import views

# TEMPLATE TAGGING
app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
]
