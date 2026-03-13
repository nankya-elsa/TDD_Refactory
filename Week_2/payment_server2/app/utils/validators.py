# helper functions that validate payment data
# used by the service layer to check amounts, currencies and emails

def validate_amount(amount):
    # check that amount is a whole number (not decimal) and greater than 0
    return isinstance(amount, int) and not isinstance(amount, bool) and amount > 0

def validate_currency(currency):
    # check that currency is a string and exactly 3 characters (e.g. "usd", "eur")
    return isinstance(currency, str) and len(currency) == 3

def validate_email(email):
    # check that email is a string and contains "@" and "."
    return isinstance(email, str) and "@" in email and "." in email