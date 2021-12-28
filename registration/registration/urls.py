from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration/', include('creation.urls')),
    path('api/users/', include('users.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
]
