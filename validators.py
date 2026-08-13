import re


def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))


def is_positive_integer(value: int) -> bool:
    return isinstance(value, int) and value > 0


def is_valid_url(url: str) -> bool:
    url_regex = r'^(http|https)://[^\s/$.?#].[^\s]*$'
    return bool(re.match(url_regex, url))


def is_non_empty_string(s: str) -> bool:
    return isinstance(s, str) and bool(s.strip())


def are_valid_coordinates(latitude: float, longitude: float) -> bool:
    return -90 <= latitude <= 90 and -180 <= longitude <= 180


def is_valid_credit_card(card_number: str) -> bool:
    card_regex = r'^(4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|7[0-9]{15})$'
    return bool(re.match(card_regex, card_number))


