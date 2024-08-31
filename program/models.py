from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class ProgramCategoryList(TimestampMixin, UserStampedMixin, models.Model):
    program_category = models.CharField('Program Category', max_length=100, null=True, unique=True)

    def __str__(self):
        return self.program_category


class ProgramList(TimestampMixin, UserStampedMixin, models.Model):
    program_name = models.CharField('Program Name', max_length=100, null=True, unique=True)
    program_category = models.ForeignKey(ProgramCategoryList, null=True, on_delete=models.PROTECT)
    registered_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.program_name)


class ProgramPlanner(TimestampMixin, UserStampedMixin, models.Model):
    program_name = models.ForeignKey(ProgramList, on_delete=models.CASCADE, null=True)
    duration = models.CharField(max_length=100, null=True)
    resources_provided = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def clean(self):
        # Call the parent class's clean method
        super().clean()

        # Validation: Check if end_date is before start_date
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date must be greater than or equal to start date.'})

    def save(self, *args, **kwargs):
        # Ensure clean() is called before saving
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.program_name)


class EvaluationNotes(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    program_name = models.ForeignKey(ProgramPlanner, on_delete=models.CASCADE, null=True)
    evaluation_notes = models.TextField()

