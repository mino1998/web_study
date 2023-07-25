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