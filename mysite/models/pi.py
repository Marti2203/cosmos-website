from django.db import models


class Pi(models.Model):
    ip = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
