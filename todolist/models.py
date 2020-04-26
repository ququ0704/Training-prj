from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Todolist(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    usrname = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.tittle