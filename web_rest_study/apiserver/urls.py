"""
URL configuration for apiserver1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from apiserverapplication import views
urlpatterns = [
    path("admin/", admin.site.urls),
    # example로 시작하는 url은 해당 애플리케이션.urls.py파일에서 처리
    path("example/", include("apiserverapplication.urls")),
    path("ajax/",views.ajax)
]