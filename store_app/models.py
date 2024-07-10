from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class MyUserManager(BaseUserManager):

    def create_user(self, name, email, password=None):
        """
            Create and save a user with the given name and email.
        """
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    objects = MyUserManager()

    USERNAME_FIELD = "email"


class Payment(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    pass


class Address(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    pass
