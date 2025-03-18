from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.create_user(email="user3@example.com",password="password123",first_name="John",last_name="Doe",mobile_no="1234567890")