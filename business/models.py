from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class ServicesProductsList(TimestampMixin, UserStampedMixin, models.Model):
    service_products = models.CharField('Service/Products', max_length=100, unique=True)

    def __str__(self):
        return self.service_products


class RegistrationStatusList(TimestampMixin, UserStampedMixin, models.Model):
    registration_status = models.CharField('Registration Status', max_length=100, unique=True)

    def __str__(self):
        return self.registration_status


class DevelopmentStageList(TimestampMixin, UserStampedMixin, models.Model):
    development_stage = models.CharField('Development Stage', max_length=100, unique=True)

    def __str__(self):
        return self.development_stage


class IndustrySectorList(TimestampMixin, UserStampedMixin, models.Model):
    industry_sector = models.CharField('Industry Sector', max_length=100, unique=True)

    def __str__(self):
        return self.industry_sector


class BusinessRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    business_model = models.CharField('Business Model', max_length=200, null=True)
    name = models.CharField('Name', max_length=200, null=True)
    location = models.CharField('Location', max_length=200, null=True)
    services_products = models.ForeignKey(ServicesProductsList, on_delete=models.PROTECT, null=True)
    registration_status = models.ForeignKey(RegistrationStatusList, on_delete=models.PROTECT, null=True)
    development_stage = models.ForeignKey(DevelopmentStageList, on_delete=models.PROTECT, null=True)
    industry_sector = models.ForeignKey(IndustrySectorList, on_delete=models.PROTECT, null=True)
    progress_metrics = models.CharField('Progress Metrics', max_length=200, null=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class OutcomeRecord(TimestampMixin, UserStampedMixin, models.Model):
    business_record = models.ForeignKey(BusinessRecord, on_delete=models.CASCADE, null=True)
    milestone_achieved = models.TextField()
    revenue = models.PositiveIntegerField()
    exit_strategy = models.TextField()