from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('comment/', views.blogComment, name='blogComment'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]