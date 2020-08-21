from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/add/<str:name>/', views.add_model)
]
