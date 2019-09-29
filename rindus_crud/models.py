from django.db import models
from django.contrib.auth.models import User
from localflavor.generic.models import IBANField

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    iban = IBANField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
