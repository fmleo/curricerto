from django.contrib.auth.models import User
from django.db import models


class UserOwned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
