from django import template

register = template.Library()

def get_persian_number(value):
    numbers = {
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
        "0": "۰"
    }
    value_string = str(value)
    for number, value in numbers.items():
        value_string = value_string.replace(number, value)

    return value_string


register.filter("get_persian_number", get_persian_number)