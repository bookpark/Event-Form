from django.db import models
from django.utils import timezone

from utils.custom_path import application_form_upload_path


class Event(models.Model):
    title = models.CharField(
        max_length=30,
    )
    event_date = models.DateField()
    close_date = models.DateTimeField()
    application_form = models.FileField(
        upload_to=application_form_upload_path
    )

    def is_past(self):
        if timezone.now() > self.close_date:
            return True
        return False

    def __str__(self):
        return f'{self.title}'


class Application(models.Model):
    event = models.ForeignKey(
        'Event',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    company = models.CharField(
        max_length=30,
    )
    name = models.CharField(
        max_length=10,
    )
    email = models.EmailField(
        max_length=50,
    )
    application = models.FileField()
    logo = models.FileField()
    business_license = models.FileField()
