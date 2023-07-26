"""
URL configuration for mysite project.

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
from django.urls import path
from myweb import views

urlpatterns = [
    # admin/요청이 오면 admin.site.urls 함수가 처리하겠다고 남김
    path("admin/", admin.site.urls),
    # 기본 요청은 ""이다. 이걸 누가 처리하면 좋을까?
    path("",views.index), # myweb에 있는 views 모듈의 index 함수가 처리할거야~
    path("template",views.template), # 앞뒤 맞추는게 기억하기 편함
    path("checkDB",views.checkDB), #얼른 views에다가 checkDB를 만들어주자.
    path("detail/<str:itemID>", views.detail) #itemID의 자료형을 알아야겠지
]
