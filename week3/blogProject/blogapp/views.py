from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all() # 블로그 모든 글들을 대상으로
    paginator = Paginator(blog_list, 3) # 블로그 객체 3개를 한 페이지로 자르기
    page = request.GET.get('page') # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    posts = paginator.get_page(page) # request된 페이지를 얻어온 뒤 return 해준다.
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail': blog_detail})

# new.html 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/'+str(blog.id))
# redirect(URL) : 위에서 완성한 데이터를 parameter로 있는 URL로 넘기는 함수

