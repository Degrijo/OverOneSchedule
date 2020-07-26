from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from address.models import AddressField
from djmoney.models.fields import MoneyField
from phone_field import PhoneField


class CustomUser(AbstractUser):
    programming_exp = models.TextField(blank=True)
    learning_groups = models.ManyToManyField('core.Group', related_name='students', through='core.UserGroup')
    education = models.ForeignKey('core.Education', on_delete=models.CASCADE, related_name='users')
    birthday = models.DateField()
    avatar = models.ImageField(blank=True, null=True, upload_to='user-avatar/')
    phone = PhoneField()


class UserGroup(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_groups')
    group = models.ForeignKey('core.Group', on_delete=models.CASCADE, related_name='user_groups')
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    STATUS_CHOICES = (
        (PENDING, _('Pending')),
        (ACCEPTED, _('Accepted')),
        (REJECTED, _('Rejected'))
    )
    status = models.PositiveSmallIntegerField(default=PENDING, choices=STATUS_CHOICES)


class Group(models.Model):
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='teaching_groups')
    way = models.ForeignKey('core.Way', on_delete=models.CASCADE, related_name='groups')
    RECRUITMENT = 0
    TRAINING = 1
    DISMISSAL = 2
    STATUS_CHOICES = (
        (RECRUITMENT, _('Recruitment')),
        (TRAINING, _('Training')),
        (DISMISSAL, _('Dismissal')),
    )
    status = models.PositiveSmallIntegerField(default=RECRUITMENT, choices=STATUS_CHOICES)

    def __str__(self):
        return '№' + str(self.id)


class Lesson(models.Model):
    date = models.DateTimeField()
    topics = models.ManyToManyField('core.Topic', related_name='lessons')
    room = models.ForeignKey('core.Room', on_delete=models.CASCADE, related_name='lessons')
    attachments = models.ManyToManyField('core.Attachment', related_name='lessons')
    group = models.ForeignKey('core.Group', on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f'{self.date} {self.group}'


class Way(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='way-logo/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='BYN')
    NO_TYPE = 0
    MONEY_TYPE = 1
    PERCENT_TYPE = 2
    DISCOUNT_CHOICES = (
        (NO_TYPE, _('No discount')),
        (MONEY_TYPE, _('Money discount')),
        (PERCENT_TYPE, _('Percent discount'))
    )
    description = models.TextField(blank=True)
    discount_type = models.PositiveSmallIntegerField(default=NO_TYPE, choices=DISCOUNT_CHOICES)
    money_discount = MoneyField(max_digits=14, decimal_places=2, default_currency='BYN', blank=True, null=True)
    percent_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.title} {"Online" if self.is_online else "Offline"}'


class WayAdvantage(models.Model):
    title = models.CharField(max_length=200)
    ways = models.ManyToManyField('core.Way', related_name='advantages')

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    parent_topic = models.ForeignKey('core.Topic', on_delete=models.CASCADE, related_name='child_topics', blank=True, null=True)
    ways = models.ManyToManyField('core.Way', related_name='topics')

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.CharField(max_length=10)
    level = models.SmallIntegerField()
    office = models.ForeignKey('core.Office', on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.number


class Office(models.Model):
    address = AddressField()

    def __str__(self):
        return self.address


class Attachment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='lessons/attachments', blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
