from django.db import models

class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.admin_id + '|' + self.email

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    admin_id = models.ForeignKey(Admin.admin_id)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    iban = models.CharField(max_length=24)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
