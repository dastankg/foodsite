from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    date_of_birth = models.DateField('Date of birth', blank=True, null=True)
    photo = models.ImageField('Photo', upload_to='users/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.username

    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'