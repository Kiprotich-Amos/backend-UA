from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

class CustomUserManager(UserManager):
    def create_superuser(self, email, first_name, last_name, mobile_no, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.model(email=email, first_name=first_name, last_name=last_name, mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile_no']

    def __str__(self):
        return self.email
    
class Role(models.Model):
    role_name = models.CharField(max_length=100)
    role_description = models.CharField(max_length=255)
    
