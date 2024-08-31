from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin
from business.models import BusinessRecord

# Create your models here.


class FundTypeList(TimestampMixin, UserStampedMixin, models.Model):
    fund_type = models.CharField('Fund Type', max_length=100, unique=True)

    def __str__(self):
        return self.fund_type


class InvestorTypeList(TimestampMixin, UserStampedMixin, models.Model):
    investor_type = models.CharField('Fund Type', max_length=100, unique=True)

    def __str__(self):
        return self.investor_type


class InvestorRecord(TimestampMixin, UserStampedMixin, models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    investor_type = models.ForeignKey(InvestorTypeList, on_delete=models.PROTECT, null=True)


class FundRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fund_type = models.ForeignKey(FundTypeList, on_delete=models.PROTECT, null=True)
    amount = models.FloatField()
    funded_by = models.CharField('Funded By', max_length=200, null=True)
    terms = models.TextField()
    date_provided = models.DateField()


class InvestmentRecord(TimestampMixin, UserStampedMixin, models.Model):
    investor = models.ForeignKey(InvestorRecord, on_delete=models.CASCADE, null=True)
    invested_in_business = models.ForeignKey(BusinessRecord, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField()
    investment_no = models.CharField(max_length=100, null=True)
    equity_stake = models.CharField(max_length=100, null=True)