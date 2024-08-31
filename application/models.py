from django.contrib.auth.models import User
from django.db import models
from program.models import ProgramPlanner

# Create your models here.


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='applications')
    program = models.ForeignKey(ProgramPlanner, on_delete=models.CASCADE, null=True, related_name='planned_program')
    requested_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

