from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    class Meta:
        db_table = "accounts"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.BigIntegerField()
    age = models.IntegerField()
    address = models.TextField()
    location = models.TextField(blank=True, null=True)
    # TODO : Location Will be changed later
    hobbies = models.CharField(max_length=255)
    workout_preferences = models.TextField()
    dietary_preferences = models.TextField()
    gender = models.CharField(
        max_length=6,
        choices=[('M', 'MALE'), ('F', 'FEMALE'), ('OTH', 'OTHERS')]
    )

    def __str__(self):
        return self.user.username
