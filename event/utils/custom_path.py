def application_form_upload_path(instance, filename):
    return f'신청서_양식_{instance.title}/{filename}'


def event_application_upload_path(instance, filename):
    return f'{instance.event.title}/{instance.company}/{filename}'
