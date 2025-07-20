# test_validators.py

from validators import is_valid_email, is_strong_password

# Tests for is_valid_email
def test_valid_email():
    assert is_valid_email("test@example.com") == True

def test_invalid_email_no_at_symbol():
    assert is_valid_email("testexample.com") == False

def test_invalid_email_no_domain():
    assert is_valid_email("test@.com") == False

def test_email_with_non_string_input():
    assert is_valid_email(12345) == False

# Tests for is_strong_password
def test_strong_password():
    assert is_strong_password("Password123") == True

def test_weak_password_too_short():
    assert is_strong_password("Pass1") == False

def test_weak_password_no_digit():
    assert is_strong_password("PasswordIsLong") == False

def test_weak_password_no_uppercase():
    assert is_strong_password("password123") == False

def test_password_with_non_string_input():
    assert is_strong_password(None) == False