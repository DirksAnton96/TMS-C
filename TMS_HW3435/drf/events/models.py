from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    meeting_time = models.DateTimeField(default=datetime.now, verbose_name='Дата')
    users = models.ManyToManyField(get_user_model(), related_name="events", verbose_name="Пользователи")

    class Meta:
        ordering = ['-meeting_time']
        indexes = [
            models.Index(fields=("meeting_time",), name="meeting_time_index")
        ]