from typing import Type


class BaseDeferredAttribute:
    def __init__(self, field_name: str, field_type: type[any]) -> None:
        self.field_name = field_name
        self.field_type = field_type

    def __set__(self, instance: any, value: any) -> None:
        instance.__dict__[self.field_name] = (
            self.field_type(value)
            if value is not None and not isinstance(value, self.field_type)
            else value
        )


class BaseStringType(str):
    def __new__(cls, value: str) -> str:
        if hasattr(cls, "validator"):
            cls.validator(value)
        return super().__new__(cls, value)
