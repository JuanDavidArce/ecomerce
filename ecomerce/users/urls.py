# Rest framework
from rest_framework.routers import DefaultRouter



# Django
from django.conf.urls import include
from django.urls import path

# Views 
from users.views import UserViewSet






router = DefaultRouter()
router.register(r'users',UserViewSet,basename='users')

urlpatterns = [
    path('',include(router.urls)),
 
]