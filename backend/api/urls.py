from django.urls import path
from .views import RegisterAPIView,LoginAPIView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path ('register-user', RegisterAPIView.as_view(),  name = 'register-user'),
    path('login/', LoginAPIView.as_view(), name='login')
]