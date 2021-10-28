import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def getpath(obj, filename):
    return "uploads/%s.%s" % (str(uuid.uuid4()).replace("-", ""), filename.split(".")[-1])


class Roles(models.Model):
    name = models.CharField(max_length=25)
    

class Phone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=-1)
    profile_picture = models.ImageField(upload_to=getpath, null=True)






