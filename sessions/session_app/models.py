from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True,max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

