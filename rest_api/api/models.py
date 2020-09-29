from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    language = models.CharField(null=True,max_length=50,verbose_name="Favorite Programming language")
    programmer = models.BooleanField(default=False,verbose_name="Likes Programming or not?")

    def __str__(self):
        return f'{self.name} - {self.id}'
