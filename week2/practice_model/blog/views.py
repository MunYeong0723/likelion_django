from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋 : Blog object들의 목록, 쿼리셋을 메소드를 이용해서 처리할 수 있음.
    return render(request, 'home.html', {'blogs': blogs})
