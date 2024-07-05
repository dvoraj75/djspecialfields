import re

from .enums import ValidationCode
from .exceptions import (
    InvalidBirthNumberFormatException,
    InvalidBirthNumberDateFormatException,
)
from .utils import get_birth_date_from_birth_number


class BirthNumberValidator:
    BIRTH_NUMBER_REGEX = re.compile(r"^(?P<birth>\d{6})/?(?P<suffix>\d{3,4})$")

    def __call__(self, value: str) -> None:
        if not (match := re.match(self.BIRTH_NUMBER_REGEX, value)):
            raise InvalidBirthNumberFormatException(
                f"Birth number: {value} has invalid format.",
                code=ValidationCode.INVALID_BIRTH_NUMBER_FORMAT,
            )

        birth, suffix = match.groupdict()["birth"], match.groupdict()["suffix"]
        year = int(birth[:2])

        if len(suffix) == 4:
            control_number = int(suffix[-1])
            modulo = int(birth + suffix[:3]) % 11

            if modulo != control_number and (
                modulo != 10 or modulo != control_number or year < 54 or year > 85
            ):
                raise InvalidBirthNumberFormatException(
                    f"Birth number: {value} has invalid format.",
                    code=ValidationCode.INVALID_BIRTH_NUMBER_FORMAT,
                )
        elif year >= 54 or 0 <= year <= 20:
            raise InvalidBirthNumberFormatException(
                f"Birth number: {value} has invalid format.",
                code=ValidationCode.INVALID_BIRTH_NUMBER_FORMAT,
            )

        try:
            get_birth_date_from_birth_number(value)
        except ValueError:
            raise InvalidBirthNumberDateFormatException(
                f"Birth number: {value} has invalid date format.",
                code=ValidationCode.INVALID_BIRTH_NUMBER_DATE_FORMAT,
            )
