from django.db import models

# Create your models here.

class PlanEntrance(models.Model):
    entry_exit_date = models.DateTimeField()
    entry_exit = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    point_of_passage = models.CharField(max_length=30)