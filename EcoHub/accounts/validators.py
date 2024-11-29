from django.core.exceptions import ValidationError


def validate_bulgarian_phone(value):
    if value.startswith("+359"):
        if len(value) != 13 or not value[1:].isdigit():
            raise ValidationError("Phone number must follow the format '+359XXXXXXXXX'.")
    elif value.startswith("0"):
        if len(value) != 10 or not value.isdigit():
            raise ValidationError("Phone number must follow the format '0XXXXXXXXX'.")
    else:
        raise ValidationError("Phone number must start with '+359' or '0'.")


def validate_username_length(value):
    if len(value) < 4:
        raise ValidationError("Username must be at least 4 characters long.")
    if len(value) > 15:
        raise ValidationError("Username must be no more than 15 characters long.")
