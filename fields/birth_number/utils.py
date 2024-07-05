from datetime import date
from .enums import Gender
from dateutil.relativedelta import relativedelta


def get_birth_date_from_birth_number(birth_number: str) -> date:
    return date(
        year=get_year_from_birth_number(birth_number),
        month=get_month_from_birth_number(birth_number),
        day=get_day_from_birth_number(birth_number)
    )


def get_year_from_birth_number(birth_number: str) -> int:
    year = int(birth_number[:2])
    return year + (2000 if year < 54 and len(birth_number) == 10 else 1900)


def get_month_from_birth_number(birth_number: str) -> int:
    year = get_year_from_birth_number(birth_number)
    month = int(birth_number[2:4])

    match month:
        case _ if month > 70 and year > 2003:
            month -= 70
        case _ if month > 50:
            month -= 50
        case _ if month > 20 and year > 2003:
            month -= 20
    return month


def get_day_from_birth_number(birth_number: str) -> int:
    if (day := int(birth_number[4:6])) > 50:
        day -= 50
    return day


def get_age_from_birth_number(birth_number: str) -> int:
    return relativedelta(date.today(), get_birth_date_from_birth_number(birth_number)).years


def get_gender_from_birth_number(birth_number: str) -> Gender:
    return Gender.FEMALE if int(birth_number[2:4]) > 50 else Gender.MALE
