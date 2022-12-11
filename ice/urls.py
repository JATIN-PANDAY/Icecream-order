from django.contrib import admin
from django.urls import path,include
from ice import views
urlpatterns = [
    path('', views.index,name='index'),
    path('contact', views.contact,name='contact'),
    path('services', views.services,name='services'),
    path('about', views.about,name='about'),
    path('order', views.order,name='order'),
    path('showpage',views.showpage,name='show'),
    path('editpage/<int:pk>',views.Editpage,name='editpage'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('user', views.userregister,name='userregister'),
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('loginuser',views.loginuser,name='loginuser    ')
# css
    # path('style', views.style,name='style'),




]
