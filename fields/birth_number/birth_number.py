from datetime import date

from .enums import Gender
from .utils import (
    get_birth_date_from_birth_number,
    get_gender_from_birth_number,
    get_age_from_birth_number,
)
from .validators import BirthNumberValidator
from fields.base import BaseDeferredAttribute, BaseStringType
from django.db.models.fields import CharField


class BirthNumber(BaseStringType):
    validator = BirthNumberValidator()

    def age(self) -> int:
        return get_age_from_birth_number(self)

    def gender(self) -> Gender:
        return get_gender_from_birth_number(self)

    def birth_date(self) -> date:
        return get_birth_date_from_birth_number(self)


class BirthNumberDeferredAttribute(BaseDeferredAttribute):
    pass


class BirthNumberField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 11
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, private_only=False):
        super().contribute_to_class(cls, name, private_only)
        setattr(
            cls, self.attname, BirthNumberDeferredAttribute(self.attname, BirthNumber)
        )
