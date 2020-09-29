from django.db import models

class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    user = models.CharField(
        max_length=50,
        verbose_name="Name",
        unique=True,
        )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
        verbose_name="Gender",
    )
    pub_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.user

class Task(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default='No user selected')
    tasks = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasks
