from django.db import models
import uuid

class AjaxModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True,max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.id}'
