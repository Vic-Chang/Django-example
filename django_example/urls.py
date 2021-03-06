"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Member', views.MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    # Use viewSet
    path('api/', include(router.urls)),
    # Use Api View
    path('api/', include('api.urls')),
    # 取得 Token 的路由
    # 可透過 `python manage.py createsuperuser --email admin@example.com --username admin` 建立帳號
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 將 home app 設為首頁
    path('', include('home.urls'))
]