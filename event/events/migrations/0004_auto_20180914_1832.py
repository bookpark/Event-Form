# Generated by Django 2.1.1 on 2018-09-14 09:32

from django.db import migrations, models
import utils.custom_path
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180914_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='phone_number',
            field=models.CharField(default=1, max_length=11, validators=[utils.validators.validate_phone_number]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(default='1', upload_to=utils.custom_path.application_form_upload_path),
            preserve_default=False,
        ),
    ]