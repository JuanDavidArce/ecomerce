"""User model"""

#django
from django.db  import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    """User model 
    Extend from djangos's abstract user, change the username field 
    to email """
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique':'A user with that email already exists'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']


