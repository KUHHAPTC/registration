from django.urls import path

from creation import views

urlpatterns = [
    path('', views.CreateUser.as_view()),
    path('<uid64>/<token>/', views.VerifyEmail.as_view()),
]
