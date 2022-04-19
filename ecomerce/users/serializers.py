# Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# Django
from django.contrib.auth import password_validation


# Models
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email","username","first_name","last_name"]



class UserSignupSerializer(serializers.Serializer):
    
    email = serializers.EmailField(validators = [UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(min_length=8,
                                    max_length=20,
                                    validators=[UniqueValidator(queryset=User.objects.all())])

    first_name = serializers.CharField(min_length = 2, max_length=20)
    last_name = serializers.CharField(min_length = 2,max_length=20)
    password = serializers.CharField(min_length = 8,max_length = 50)
    password_confirmation = serializers.CharField(min_length = 8,max_length = 50)


    def validate(self, attrs):
        passw = attrs['password']
        passw_confirmation = attrs['password_confirmation']

        if passw != passw_confirmation:
            raise serializers.ValidationError({'Passwords':'Passwords do not match'})
        password_validation.validate_password(passw)

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data)
        return user