from django.db import models


class Door(models.Model):
    is_open = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
