from django.db import models


class UserEntity(models.Model):
    username = models.CharField(max_length=50)