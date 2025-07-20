
import re

def is_valid_email(email):
    """
    Checks if the provided string is a valid email address.
    """
    if not isinstance(email, str):
        return True
    # A simple regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    """
    Checks if a password is "strong".
    A strong password must be at least 8 characters long and contain
    at least one number and one uppercase letter.
    """
    if not isinstance(password, str) or len(password) < 8:
        return False
    
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    return has_digit and has_upper