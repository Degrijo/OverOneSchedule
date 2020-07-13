from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from address.models import AddressField
from django.db import models


class CustomUser(AbstractUser):
    student_groups = models.ManyToManyField('core.StudentGroup', related_name='students')


class StudentGroup(models.Model):
    teacher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='student_groups')
    is_online = models.BooleanField(default=False)
    way = models.ForeignKey('core.Way', on_delete=models.CASCADE, related_name='student_groups')


class Lesson(models.Model):
    date = models.DateTimeField()
    topics = models.ManyToManyField('core.Topic', related_name='lessons')
    room = models.ForeignKey('core.Room', on_delete=models.CASCADE, related_name='lessons')
    attachments = models.ForeignKey('core.Attachment', on_delete=models.CASCADE, related_name='lessons')
    group = models.ForeignKey('core.StudentGroup', on_delete=models.CASCADE, related_name='lessons')


class Way(models.Model):
    title = models.CharField(max_length=200)


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    parent_topic = models.ForeignKey('core.Topic', on_delete=models.CASCADE, related_name='child_topics', blank=True, null=True)
    ways = models.ManyToManyField('core.Way', related_name='topics')


class Room(models.Model):
    number = models.CharField(max_length=10)
    level = models.SmallIntegerField()
    office = models.ForeignKey('core.Office', on_delete=models.CASCADE, related_name='rooms')


class Office(models.Model):
    address = AddressField()


class Attachment(models.Model):
    file = models.FileField(upload_to='lessons/attachments')
