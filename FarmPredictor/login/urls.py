from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('callback/',views.callback),
    path('logout/',views.logout),
    path('region/',views.region),
    path('submit/',views.submit),
]