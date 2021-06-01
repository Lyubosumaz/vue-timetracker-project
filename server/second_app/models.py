from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=255, unique=True)
