import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def getpath(obj, filename):
    return "uploads/%s.%s" % (str(uuid.uuid4()).replace("-", ""), filename.split(".")[-1])


class Roles(models.Model):
    name = models.CharField(max_length=25)
    

class Picture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=-1)
    profile_picture = models.ImageField(upload_to=getpath, null=True)


class Org(models.Model):
    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=-1)


class Project(models.Model):
    name = models.CharField(max_length=25)
    org = models.ForeignKey(Org, on_delete=models.CASCADE, default=-1)


class ProjectColumn(models.Model):
    name = models.CharField(max_length=25)


