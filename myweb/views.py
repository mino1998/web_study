import django.shortcuts
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # HTML을 직접 작성해서 출력하기
    # return HttpResponse("<h1>Hello Django</h1>")
    # HTML 파일을 가져오기
    return render(request, 'index.html')

def template(request):
    msg="Hello Django Tmeplate"
    person={"name":"mino", "age":26}
    data=["mino","mino2","mino3","mino4","mino5","mino6","mino7"]
    #html에 데이터를 전송하고자 한다면
    # 세 번째 변수에 딕셔너리를 만들어서
    # 데이터 이름과 데이터를 기재
    return render(request, 'template.html', {"msg":msg, "person":person, "data":data})

from myweb.models import Item
def checkDB(request):
    dbData=Item.objects.all()
    print(dbData)
    return render(request, 'checkDB.html', {"dbData":dbData})

def detail(request, itemID): #하나를 받는다면 그거 그대로 써오자.
    item=Item.objects.get(itemID=itemID)
    print(item)
    return render(request, 'detail.html', {"item":item})
