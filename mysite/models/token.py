from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=100)
    device = models.CharField(max_length=50)  # the target entity that uses this token
