from django.db import models
from django.utils import timezone
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
            name=name,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = "email"


class Payment(models.Model):
    """
        Store payment info
    """
    UPI = 'U'
    Credit_Card = 'CC'
    Payment_Method_Choies = [
        (UPI, "UPI"),
        (Credit_Card, "Credit Card"),
    ]
    payment_method = models.CharField(
        max_length=255, choices=Payment_Method_Choies, default=UPI)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True, default=timezone.now)


class Address(models.Model):
    """
        store Addresses for each user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    country = models.CharField(max_length=255, default='iran')
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address_line = models.TextField(blank=True, null=True)

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
