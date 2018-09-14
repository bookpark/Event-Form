from django.db import models
from django.utils import timezone

from utils.custom_path import application_form_upload_path, event_application_upload_path


class Event(models.Model):
    title = models.CharField(
        max_length=30,
    )
    event_date = models.DateField()
    close_date = models.DateTimeField()
    application_form = models.FileField(
        upload_to=application_form_upload_path
    )

    # 신청 종료 날짜가 지나면 True 값을 리턴
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
    event_application = models.FileField(
        upload_to=event_application_upload_path
    )
    logo = models.FileField(
        upload_to=event_application_upload_path
    )
    business_license = models.FileField(
        upload_to=event_application_upload_path
    )

    # 행사 신청 기간이 지난 후 url로 접근해 신청을 해도 신청되지 않도록 save() 값 오버라이드
    def save(self, *args, **kwargs):
        if self.event.close_date < timezone.now():
            raise Exception('행사 신청 가능 기간이 지났습니다')
        super(Application, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.event} - {self.company}'
