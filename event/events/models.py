from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(
        max_length=30,
    )
    event_date = models.DateField()
    close_date = models.DateTimeField()
    application_form = models.FileField()

    def is_past(self):
        if timezone.now() > self.close_date:
            return True
        return False


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
