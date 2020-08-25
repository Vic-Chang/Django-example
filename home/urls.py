from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/add/<str:name>/', views.add_model),
    path('home/del/<int:user_id>/', views.del_model),
    path('home/update/<int:user_id>/<str:name>/', views.update_model),
    path('home/read/<int:user_id>/', views.read_model)

]
