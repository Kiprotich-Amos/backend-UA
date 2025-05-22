from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from .models import User,Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'mobile_no', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
        read_only_fields = ['id', 'date_joined', 'is_staff', 'is_superuser']



class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile_no', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        validated_data['username'] = validated_data['email']  # Add username
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

    def create(self, validated_data):
        refresh = RefreshToken.for_user(validated_data)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(validated_data).data, #return user data
        }

class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    modified_by = UserSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__' # or specify the fields you want to expose
        read_only_fields = ('last_modified', 'modified_by') # make these read only.

    def create(self, validated_data):
      # Ensure user is set on create
      user = self.context['request'].user
      company = Company.objects.create(user=user, **validated_data)
      return company

    def update(self, instance, validated_data):
      # Ensure modified by is set on update
      user = self.context['request'].user
      for attr, value in validated_data.items():
          setattr(instance, attr, value)
      instance.save(modified_user=user) #Pass the user using the custom save method.
      return instance