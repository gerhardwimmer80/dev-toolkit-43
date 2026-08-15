import re

class DataValidator:
    def __init__(self):
        self.email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_regex = r'^(\+?\d{1,3}[- ]?)?\(?\d{1,4}?\)?[- ]?\d{1,4}[- ]?\d{1,4}[- ]?\d{1,9}$'

    def validate_email(self, email):
        if re.match(self.email_regex, email):
            return True
        return False

    def validate_phone(self, phone):
        if re.match(self.phone_regex, phone):
            return True
        return False

    def validate_username(self, username):
        if 3 <= len(username) <= 30 and re.match('^[a-zA-Z0-9_]+$', username):
            return True
        return False

# Example usage:
# validator = DataValidator()
# print(validator.validate_email('test@example.com'))
# print(validator.validate_phone('+123-456-7890'))
# print(validator.validate_username('user_name_123'))
