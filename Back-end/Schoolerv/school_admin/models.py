from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    housename = models.CharField(max_length=30)
    post = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40)
    pin = models.BigIntegerField()
    subject = models.CharField(max_length=40)

    class Meta:
        db_table = 'teacher'