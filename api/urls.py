from django.urls import path
from api import views

urlpatterns = [
    path('checkbox_list/', views.CheckboxList.as_view(), name='checkbox_list'),
    path('data/', views.DataView.as_view()),
]
