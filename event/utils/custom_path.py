def application_form_upload_path(instance, filename):
    return f'{instance.title}/{filename}'


def event_application_upload_path(instance, filename):
    return f'{instance.event.title}/{instance.company}/{filename}'
