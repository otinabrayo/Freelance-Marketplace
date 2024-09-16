from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='getToken'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refreshToken'),
    path('', include('Market.urls'))
]
