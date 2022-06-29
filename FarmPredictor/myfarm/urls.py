from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.myfarm),
    path('select_crop/', views.select_crop),
]