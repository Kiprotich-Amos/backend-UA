from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from django.core.exceptions import ValidationError


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
    
    def clean(self):
        super().clean()
        try:
            parsed_number = phonenumbers.parse(self.mobile_no, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid mobile number")
            self.mobile_no = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        except NumberParseException:
            raise ValidationError("Invalid mobile number format")

    def __str__(self):
        return self.email
 