from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class RawForm(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Name",
        )
    age = models.IntegerField(
        verbose_name="Age",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="Email",
        )
    birthday = models.DateField(verbose_name="Birthday")
    language = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name="Favorite Programming language",
        )
    programmer = models.BooleanField(default=False,verbose_name="Likes Programming or not?")

    def __str__(self):
        return self.name
