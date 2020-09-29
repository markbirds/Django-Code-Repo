import uuid
from django.db import models

class DisplayViewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True,max_length=50)
    age = models.IntegerField()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('display_views:detail_view', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} - {self.id}'
