from django.db import models

# Create your models here.
class Registration(models.Model):
    team_name = models.CharField(max_length=40)
    project_name = models.CharField(max_length=30)
    lead_contact = models.EmailField(max_length=30)
    member1 = models.CharField(max_length=40)
    member2 = models.CharField(max_length=40)
    member3 = models.CharField(max_length=40)
    member4 = models.CharField(max_length=40)
