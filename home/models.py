from django.contrib.auth.models import User
from django.db import models

from utils import TimestampMixin, UserStampedMixin


# Create your models here.

class Gender(TimestampMixin, UserStampedMixin, models.Model):
    gender = models.CharField('Gender', max_length=10)

    def __str__(self):
        return self.gender


class UserRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField('First Name', max_length=50)
    middle_name = models.CharField('Middle Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.first_name + " " + self.middle_name


class PhoneRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField('Phone Number', max_length=15)


class WhatsappNumRec(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    whatsapp_number = models.CharField('Whatsapp Number', max_length=15, null=True)


class EmailRecord(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField('Email', null=True)


class Skill(TimestampMixin, UserStampedMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skill = models.EmailField('skill', null=True)


class ProfileImage(TimestampMixin, UserStampedMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='media/profile_image/')

    def __str__(self):
        return str(self.user)
