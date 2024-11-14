from django.db import models


class UserEntity(models.Model):
    class Meta:
        app_label = 'entity'
    username = models.CharField(max_length=50)