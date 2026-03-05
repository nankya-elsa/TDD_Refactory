from account import receive_payment, update_transaction_history, make_payment

# Test for receive_payment function
def test_receive_payment():
    account = "MTN Mobile Money"
    amount = 150000
    Notification = receive_payment(account, amount)
    assert Notification == f"Received payment of {amount}"

# Test for update_transaction_history function
def test_update_transaction_history():
    account = "MTN Mobile Money"
    transaction = f"Received payment of 150000"
    Notification = update_transaction_history(account, transaction)
    assert Notification == f"Updated transaction history with: {transaction}"

# Test for make_payment function
def test_make_payment():
    account = "MTN Mobile Money"
    amount = 50000
    Notification = make_payment(account, amount)
    assert Notification == f"Made payment of {amount}"