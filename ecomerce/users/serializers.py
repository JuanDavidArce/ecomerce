# Rest Framework
from rest_framework.serializers import ModelSerializer


# Models
from users.models import User


class UserModelSerializer(ModelSerializer):

    class Meta:
        "Meta class"
        model = User
        fields = ["first_name","last_name","email","password"]