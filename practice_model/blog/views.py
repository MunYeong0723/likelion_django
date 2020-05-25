from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects # 쿼리셋 : Blog object들의 목록, 쿼리셋을 메소드를 이용해서 처리할 수 있음.
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    # get_object_or_404(객체, pk) : object를 가지고 오기도 하고(get_object), 예외처리(or_404)'도' 해주는 역할
    blog_detail = get_object_or_404(Blog, pk=blog_id) # blog_id번째의 blog(객체)를 넘김.
    return render(request, 'detail.html', {'blog': blog_detail})
