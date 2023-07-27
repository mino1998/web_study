from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET']) #요청 처리 방식 선택
def helloAPI(request):
    return Response("HELLO REST API")

from .serializers import BookSerializer
from rest_framework import status
from .models import Book
@api_view(['POST', 'GET', 'PUT','DELETE']) #post, get 둘다 처리할 수 있는데, 구분은 해놔야 할것 같아.
def booksAPI(request):
    #전송 방식을 확인하는 방법은 request.method를 확인하면 됩니다.
    if request.method=='GET':
        # 전체 데이터 가져오기
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST': #post일때
        # 클라이언트가 전송한 데이터를
        # Model이 사용할 수 있는 데이터로 변환
        # print("1") # 이 코드가 실행 안된다면url과 method 연결 실수
        serializer = BookSerializer(data=request.data)
        # print("2") # 이 코드가 실패했다면, serializable 실패
        # 유효성 검사
        if serializer.is_valid():
            # print("3") # 이 코드가 안된다면, 이름이 잘못된 것이다.
            serializer.save()  # 데이터 저장
            # 성공했을 때 전송한 데이터를 다시 전송
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        # 실패했을 때 처리
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#기본키를 가지고 데이터를 찾아오고 없다면 404error 발생을 하겠다.
from rest_framework.generics import get_object_or_404

@api_view(['GET','PUT'])
def bookAPI(request, bid): #bid가 url에 포함되어있다.
    #기본키를 가지고 데이터 1개를 가져오는 것입니다.
    # books=get_object_or_404(Book, bid=bid) try except 대신 이걸 쓰지 그냥
    try:
        books = Book.objects.get(bid=bid)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=BookSerializer(books)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_404_NOT_FOUND)


from django.shortcuts import render
def ajax(request):
    return render(request, "ajax.html")