from enum import Enum


class ValidationCode(Enum):
    INVALID_BIRTH_NUMBER_FORMAT = "invalid_birth_number_format"
    INVALID_BIRTH_NUMBER_DATE_FORMAT = "invalid_birth_number_date_format"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
