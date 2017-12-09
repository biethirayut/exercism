from datetime import timedelta


def add_gigasecond(birth_date):
    birth_date += timedelta(seconds=10 ** 9)
    return birth_date

