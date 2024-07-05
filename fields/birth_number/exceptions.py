from django.core.exceptions import ValidationError


class InvalidBirthNumberFormatException(ValidationError):
    pass


class InvalidBirthNumberDateFormatException(InvalidBirthNumberFormatException):
    pass
