from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
    path('maps/', views.maps, name="maps"),
    path('pictures/', views.pictures, name="pictures"),
]

