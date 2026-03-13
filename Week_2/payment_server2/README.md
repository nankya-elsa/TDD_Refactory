# Payment Server 2 — TDD Assignment

A fake payment server built with Flask and unittest using Test-Driven Development (TDD). No real money, no real cards, no real database. All data lives in memory. The goal is the test suite.

---

## Tech Stack

- **Python** — programming language
- **Flask** — web framework for building the API
- **unittest** — Python's built-in testing framework
- **pytest** — test runner

---

## Project Structure

```
payment_server2/
├── app/
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py        ← Task 1 — validation helper functions
│   ├── services/
│   │   ├── __init__.py
│   │   └── payment_service.py   ← Task 2 — business logic layer
│   ├── repos/
│   │   ├── __init__.py
│   │   └── fake_payment_repo.py ← Task 3 — fake in-memory database
│   └── routes/
│       ├── __init__.py
│       ├── customers.py         ← Task 4 — customer HTTP endpoints
│       └── payments.py          ← Task 4 — payment HTTP endpoints
└── tests/
    ├── __init__.py
    ├── test_validators.py       ← Task 1 tests
    ├── test_payment_service.py  ← Task 2 tests
    ├── test_fake_repo.py        ← Task 3 tests
    └── test_routes.py           ← Task 4 & 5 tests
```

---

## Setup

**1. Clone the repo**
```bash
git clone <your-repo-url>
cd payment_server2
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install flask pytest
```

---

## Running the Tests

```bash
# run all tests
pytest -v

# run tests for a specific task
pytest tests/test_validators.py -v
pytest tests/test_payment_service.py -v
pytest tests/test_fake_repo.py -v
pytest tests/test_routes.py -v
```

---

## The Three Layers

This project is built in three separate layers, each with its own job and its own tests:

**1. Repository** (`fake_payment_repo.py`)
The fake database. Just Python dictionaries storing everything in memory. Its only job is saving and fetching data — no business logic.

**2. Service** (`payment_service.py`)
Where all the business rules live. Things like "amount must be a positive integer" or "you can't refund a failed payment." The service doesn't know about HTTP at all — it just takes data, applies rules, and calls the repository.

**3. Routes** (`customers.py`, `payments.py`)
The HTTP layer — the actual Flask endpoints. Routes receive requests, call the service, and send back responses. They don't contain business logic.

---

## What We Implemented — 5 Tests Per Task

### Task 1 — Validation Helpers (5 tests)
Pure helper functions with no dependencies. They take a value and return True or False.

| Test | What it checks |
|------|----------------|
| `test_validate_amount_returns_true_for_valid_amount` | 100 is a valid positive integer → True |
| `test_validate_amount_returns_false_for_zero` | 0 is not valid → False |
| `test_validate_amount_returns_false_for_decimal` | 9.99 is a decimal → False |
| `test_validate_currency_returns_true_for_valid_currency` | 'usd' is exactly 3 chars → True |
| `test_validate_email_returns_true_for_valid_email` | 'alice@gmail.com' contains @ and . → True |

### Task 2 — PaymentService (5 tests)
Business logic layer. The FakeRepository is injected into the service so tests are independent of any database.

| Test | What it checks |
|------|----------------|
| `test_create_customer_returns_correct_name_and_email` | Customer is created with correct name and email |
| `test_create_customer_raises_error_when_name_is_empty` | Raises ValueError 'Name is required' |
| `test_create_payment_returns_payment_with_pending_status` | Payment is created with status 'pending' |
| `test_create_payment_raises_error_when_amount_is_zero` | Raises ValueError 'Invalid amount' |
| `test_capture_payment_changes_status_to_succeeded` | Status changes from pending to succeeded |

### Task 3 — FakeRepository (5 tests)
Tests the fake in-memory database itself to prove it stores and retrieves data correctly.

| Test | What it checks |
|------|----------------|
| `test_save_customer_stores_and_find_customer_by_id_returns_it` | Save then fetch returns same customer |
| `test_find_customer_by_id_returns_none_for_unknown_id` | Unknown id returns None |
| `test_save_payment_stores_and_find_payment_by_id_returns_it` | Save then fetch returns same payment |
| `test_find_customer_by_email_returns_customer_when_email_matches` | Email lookup returns correct customer |
| `test_clear_empties_all_stored_data` | clear() wipes everything |

### Task 4 — Routes (5 tests)
HTTP layer tests. The service is mocked so route tests only check HTTP behaviour — correct status codes and response shapes.

| Test | What it checks |
|------|----------------|
| `test_post_customers_returns_201_with_valid_input` | Valid input → 201 + customer object |
| `test_post_customers_returns_400_when_name_is_missing` | Missing name → 400 |
| `test_post_payments_returns_201_with_valid_input` | Valid input → 201 + payment object |
| `test_post_payments_returns_400_when_amount_is_missing` | Missing amount → 400 |
| `test_post_capture_returns_200_when_capture_succeeds` | Capture succeeds → 200 + updated payment |

### Task 5 — Edge Cases (5 tests)
Boundary tests, 404s, and error handling.

| Test | What it checks |
|------|----------------|
| `test_post_payments_amount_of_1_returns_201` | Minimum valid amount → 201 |
| `test_post_payments_amount_of_0_returns_400` | Zero amount → 400 |
| `test_post_payments_amount_of_negative_returns_400` | Negative amount → 400 |
| `test_get_customer_unknown_id_returns_404` | Unknown customer id → 404 |
| `test_get_payment_unknown_id_returns_404` | Unknown payment id → 404 |

---

## Full Assignment Requirements

The full assignment requires 60+ tests across all five tasks. Below is the complete list.

### Task 1 — All 16 Validator Tests Required

1. validateAmount returns true for 100
2. validateAmount returns true for 1 (minimum boundary)
3. validateAmount returns false for 0
4. validateAmount returns false for -1
5. validateAmount returns false for 9.99 (decimal)
6. validateAmount returns false for null
7. validateAmount returns false for a string like '100'
8. validateCurrency returns true for 'usd'
9. validateCurrency returns false for 'us' (too short)
10. validateCurrency returns false for 'usdd' (too long)
11. validateCurrency returns false for an empty string
12. validateEmail returns true for 'alice@example.com'
13. validateEmail returns false for a string with no '@'
14. validateEmail returns false for an empty string
15. generateId returns a string starting with the given prefix
16. generateId returns a different value on each call

### Task 2 — All 22 PaymentService Tests Required

1. createCustomer() returns a customer with the correct name and email
2. createCustomer() generates a unique id prefixed with 'cus_'
3. createCustomer() throws 'Name is required' when name is empty
4. createCustomer() throws 'Invalid email' when email has no '@'
5. createCustomer() throws 'Email already exists' when email is registered twice
6. createPayment() returns a payment with status 'pending'
7. createPayment() generates a unique id prefixed with 'pay_'
8. createPayment() throws 'Customer not found' when customerId is unknown
9. createPayment() throws 'Invalid amount' when amount is 0
10. createPayment() throws 'Invalid amount' when amount is negative
11. createPayment() throws 'Invalid amount' when amount is a decimal like 9.99
12. createPayment() throws 'Invalid currency' when currency is not 3 characters
13. capture() changes payment status from 'pending' to 'succeeded'
14. capture() throws 'Payment not found' when id is unknown
15. capture() throws 'Cannot capture' when payment status is already 'succeeded'
16. capture() throws 'Cannot capture' when payment status is 'failed'
17. fail() changes payment status from 'pending' to 'failed'
18. refund() throws 'Payment not found' when paymentId is unknown
19. refund() succeeds when refund amount equals exactly the payment amount
20. refund() throws 'Refund exceeds payment amount' when refund is greater than payment
21. refund() throws 'Cannot refund' when payment status is 'pending'
22. refund() throws 'Cannot refund' when payment status is 'failed'

### Task 3 — All 8 FakeRepository Tests Required

1. saveCustomer() stores a customer so findCustomerById() returns it
2. findCustomerById() returns null for an unknown id
3. findCustomerByEmail() returns the customer when email matches
4. findCustomerByEmail() returns null when email does not match
5. savePayment() stores a payment so findPaymentById() returns it
6. findPaymentsByCustomer() returns only payments for the given customerId
7. findRefundsByPayment() returns all refunds linked to a payment
8. clear() empties all stored data

### Task 4 — All 18 Route Tests Required

**POST /customers (4 tests)**
1. returns 201 and the new customer object on valid input
2. returns 400 when name is missing from the body
3. returns 400 when email is missing from the body
4. service.createCustomer() is NOT called when input is invalid

**POST /payments (5 tests)**
5. returns 201 and the payment with status 'pending' on valid input
6. returns 400 when amount is missing
7. returns 400 when currency is missing
8. returns 400 when customerId is missing
9. returns 500 with { error: 'Something went wrong' } when service throws unexpectedly

**POST /payments/:id/capture (3 tests)**
10. returns 200 and the updated payment when capture succeeds
11. returns 404 when payment id is unknown
12. returns 409 when payment cannot be captured (already succeeded or failed)

**POST /refunds (4 tests)**
13. returns 201 and the refund object on valid input
14. returns 400 when paymentId is missing
15. returns 400 when amount is missing
16. returns 422 when refund amount exceeds the payment amount

**GET /payments (2 tests)**
17. returns 200 and a list of all payments
18. returns 500 when service throws unexpectedly

### Task 5 — All Edge Case Tests Required

**Boundary value tests — payment amounts**
1. POST /payments — amount of 1 (minimum) → 201
2. POST /payments — amount of 0 → 400
3. POST /payments — amount of -1 → 400
4. POST /payments — amount of 9.99 (decimal) → 400
5. POST /refunds — refund amount equal to payment amount → 201
6. POST /refunds — refund amount one penny over the payment amount → 422

**Boundary value tests — customer name length**
7. POST /customers — name of 1 character → 201
8. POST /customers — name of 100 characters → 201
9. POST /customers — name of 101 characters → 400

**Not-found tests (404)**
10. GET /customers/:id — unknown id → 404 + { error: 'Customer not found' }
11. GET /customers/:id/payments — unknown customer id → 404
12. GET /payments/:id — unknown id → 404 + { error: 'Payment not found' }
13. POST /payments/:id/capture — unknown id → 404
14. POST /payments/:id/fail — unknown id → 404
15. GET /refunds/:id — unknown id → 404 + { error: 'Refund not found' }

**Input variation tests**
16. POST /payments — no body at all → 400
17. POST /payments — amount: null → 400
18. POST /payments — currency: "" (empty string) → 400
19. POST /customers — email with no '@' → 400
20. POST /customers — same email twice → 409 Conflict

**Unexpected failure (500) tests**
21. GET /payments — service throws → 500 + { error: 'Something went wrong' }
22. POST /payments — service throws after validation passes → 500
23. POST /refunds — service throws → 500

---

## TDD Approach

This project was built strictly test-first. The flow for every single feature was:

```
1. Write a failing test (RED)           🔴
2. Define the function with pass        🔴 — still fails, for the right reason
3. Implement the minimum code (GREEN)   🟢 — test passes
4. Clean up the code (REFACTOR)         🟢 — still passes
5. Move to the next test
```

No implementation code was written before a failing test existed for it.

---

## Reflection

Building this project test-first completely changed how I approached writing code. Before TDD the instinct is to jump straight into writing functions and routes and figure out testing later. Doing it the other way around — writing the test first, watching it fail, then writing just enough code to make it pass — forces you to think clearly about what a feature should actually do before you build it.

The three layer architecture was the biggest new concept in this project. Separating the repository, service and routes means each layer can be tested in complete isolation. The service never touches HTTP. The routes never contain business logic. The repository just stores and fetches. This separation makes the code cleaner, easier to test, and easier to change without breaking everything else.
