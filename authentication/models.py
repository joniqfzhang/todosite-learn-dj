from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    # string representation of an obj
    def __str__(self):
        return self.email
    #
    # def set_email_verified(self):
    #     self.is_email_verified = models.BooleanField(True)
