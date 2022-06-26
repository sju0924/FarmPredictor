from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.predict_home),
    path('search/', views.predict_search),
    path('result/', views.predict_result),
]