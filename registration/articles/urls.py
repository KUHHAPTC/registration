from django.urls import path

from articles import views

urlpatterns = [
    path('', views.UserArticleView.as_view()),
    path('<title>/', views.UserArticleDetailView.as_view()),
]
