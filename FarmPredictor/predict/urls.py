from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.predict_search),
    path('result/', views.predict_result),
]