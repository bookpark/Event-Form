from django.core.exceptions import ValidationError


def validate_phone_number(value):
    value = value.replace('-', '')
    if len(value) not in (10, 11):
        raise ValidationError('전화번호 길이가 올바르지 않습니다.')
    if not value.startswith('0'):
        raise ValidationError('올바른 전화번호가 아닙니다.')
