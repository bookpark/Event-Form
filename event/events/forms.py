from django import forms

from events.models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = (
            'company',
            'name',
            'email',
            'phone_number',
            'event_application',
            'logo',
            'business_license',
        )
