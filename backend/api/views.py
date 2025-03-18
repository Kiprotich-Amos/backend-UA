# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterUserSerializer, LoginUserSerializer
from django.contrib.auth import authenticate

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # refresh = RefreshToken.for_user(user)
            # access_token = str(refresh.access_token)
            # refresh_token = str(refresh)
            return Response({
                'message': 'Your Registration is Successful',
                # 'access_token': access_token,
                # 'refresh_token': refresh_token
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Registration Failed!',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response({
                'message': 'Login Successful',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Login Failed!',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
