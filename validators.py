import re

def is_email_valid(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_password_strong(password: str) -> bool:
    min_length = 8
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    return len(password) >= min_length and has_digit and has_special


def is_username_valid(username: str) -> bool:
    pattern = r'^[a-zA-Z0-9._-]{3,20}$'
    return re.match(pattern, username) is not None


def validate_user_data(email: str, password: str, username: str) -> dict:
    return {
        'email_valid': is_email_valid(email),
        'password_strong': is_password_strong(password),
        'username_valid': is_username_valid(username)
    }