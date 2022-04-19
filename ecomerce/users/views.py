# Rest framework
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins,status
from rest_framework.decorators import action
from rest_framework.response import Response


# Models
from users.models import User


# Serializers
from users.serializers import UserModelSerializer,UserSignupSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                GenericViewSet):
    """Users view set.
    
    Handle login , signup , update and retrieve
    """
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserModelSerializer

    @action(methods = ["POST"],detail = False)
    def signup(self,request):
        """User signup"""
        serializer = UserSignupSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserModelSerializer(user).data
        return Response(data = user_data, status = status.HTTP_201_CREATED)