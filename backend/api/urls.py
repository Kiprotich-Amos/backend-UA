from django.urls import path
from .viewpoint.auth import LoginAPIView, RegisterAPIView, RoleAPIView
# from .viewpoint.role_views import  RoleAPIView
from rest_framework_simplejwt.views import TokenRefreshView


# urlpatterns = [
#     # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path ('register-user', RegisterAPIView.as_view(),  name = 'register-user'),
#     path('login/', LoginAPIView.as_view(), name='login')
# ]

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('roles/', RoleAPIView.as_view(), name='roles'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]