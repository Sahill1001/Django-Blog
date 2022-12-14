from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.search, name='Contact'),
    path('signup/', views.handleUser, name='HandleUser'),
    path('login/', views.handleLogin, name='HandleLogin'),
    path('logout/', views.handleLogout, name='HandleLogout'),
]