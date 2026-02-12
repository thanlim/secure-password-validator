from app.validator import validate_password

def test_valid_password():
    assert validate_password("Secure123!") is True

def test_short_password():
    assert validate_password("S1!") is False

def test_missing_uppercase():
    assert validate_password("secure123!") is False

def test_missing_digit():
    assert validate_password("SecurePass!") is False

def test_missing_special_char():
    assert validate_password("Secure123") is False

