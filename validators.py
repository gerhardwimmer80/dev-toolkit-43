import re

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_phone_number(phone: str) -> bool:
    pattern = r'^[0-9]{10}$'
    return bool(re.match(pattern, phone))


def validate_username(username: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.-]{3,15}$'
    return bool(re.match(pattern, username))


def validate_password(password: str) -> bool:
    length_valid = len(password) >= 8
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    return length_valid and has_upper and has_lower and has_digit


def validate_url(url: str) -> bool:
    pattern = r'^(http|https)://[\w.-]+(?:\.[\w.-]+)+[/\w%_.-~:?&=]*$'
    return bool(re.match(pattern, url))