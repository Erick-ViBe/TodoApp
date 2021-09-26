from django.db import models
from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)
    done = models.BooleanField(default=False)