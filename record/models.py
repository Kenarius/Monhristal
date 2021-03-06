from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Records(models.Model):
    name = models.CharField(max_length=150)

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_data')

    publish = models.DateTimeField(default=timezone.now)

    RECORD_TYPE = [
        ('photo', 'Фотосессия'),
        ('obj_shoot', 'Предметная съёмка'),
        ('make_up', 'Макияж'),
    ]
    record_type = models.CharField(max_length=30,
                                   choices=RECORD_TYPE,
                                   default='photo')

    day = models.DateField()


class Review(models.Model):
    name = models.CharField(max_length=150)

    photo = models.ImageField(upload_to="user/%Y/%m/%d/", blank=True)

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    publish = models.DateTimeField(default=timezone.now)

    RECORD_TYPE = [
        ('photo', 'Фотосессия'),
        ('obj_shoot', 'Предметная съёмка'),
        ('make_up', 'Макияж'),
    ]
    record_type = models.CharField(max_length=30,
                                   choices=RECORD_TYPE,
                                   default='photo')



