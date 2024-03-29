from django.contrib.auth.models import User
from django.db import models

class Secret(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()

    class Meta:
        db_table = "secrets"