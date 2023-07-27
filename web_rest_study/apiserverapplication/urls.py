from django.urls import path
from .views import helloAPI, booksAPI,bookAPI #views.py에서 만든다.
urlpatterns = [
    #/example/hello/ 요청이 오면 helloAPI 함수가 처리
    path("hello/", helloAPI),
    #/example/fbv/books 요청이 오면 booksAPI 함수가 처리
    path("fbv/books", booksAPI),
    #이번엔 bid 1개마다 데이터 조회하기
    path("fbv/books/<int:bid>/",bookAPI)

]
