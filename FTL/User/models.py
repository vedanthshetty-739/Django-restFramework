from django.db import models

# Create your models here.
class CustomUser(models.Model):
    id = models.CharField(max_length=100,primary_key = True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def __str__(self):
        return self.real_name

class UserActivity(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
