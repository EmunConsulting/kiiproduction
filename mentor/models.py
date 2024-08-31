from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin
from program.models import ProgramPlanner

# Create your models here.


class MentorList(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    expertise = models.TextField(null=True)
    assigned_on = models.DateField()
    assigned_until = models.DateField()

    def __str__(self):
        return str(self.user)


class Mentorship(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mentor = models.ForeignKey(MentorList, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(ProgramPlanner, on_delete=models.CASCADE, null=True)
    assigned_on = models.DateField()
    assigned_until = models.DateField()


class MentorComRec(TimestampMixin, UserStampedMixin, models.Model):
    mentorship = models.ForeignKey(Mentorship, on_delete=models.CASCADE, null=True)
    noted_on = models.DateField(auto_now_add=True, null=True)
    comment = models.TextField()
    recommendation = models.TextField()

