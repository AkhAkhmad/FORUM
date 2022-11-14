from django.urls import path
from service import views

urlpatterns = [
    path('', views.index, name='index'),
]
