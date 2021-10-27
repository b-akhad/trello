import uuid

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


def getpath(obj, filename):
    return "uploads/%s.%s" % (str(uuid.uuid4()).replace("-", ""), filename.split(".")[-1])


class Roles(models.Model):
    name = models.CharField(max_length=25)
    

class Phone(models.Model):
    phone_number = models.CharField(max_length=12, default="-1", null=True)

