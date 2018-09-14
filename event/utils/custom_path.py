def application_form_upload_path(instance):
    return f'application_form_{instance.event.title}'
