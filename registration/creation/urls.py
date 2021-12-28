from django.urls import path

from creation import views

urlpatterns = [
    path('', views.CreateUser.as_view()),
]
