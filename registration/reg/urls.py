from django.urls import path

from reg import views

urlpatterns = [
    path('', views.CreateUser.as_view()),
    path('hello/', views.HelloView.as_view()),
]