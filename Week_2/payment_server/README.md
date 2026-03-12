# Payment Server

A fake payment server built with Flask and unittest using Test-Driven Development (TDD). No real money moves. No real card networks. All data lives in memory. The goal is the test suite.

---

## What It Does

This is a sandbox payment API that simulates:

- Creating and fetching customers
- Creating payments linked to customers
- Updating payment status (pending → succeeded / failed)
- Creating refunds against succeeded payments
- Enforcing business rules (e.g. refund cannot exceed payment amount)

---

## Tech Stack

- **Python** — programming language
- **Flask** — web framework for building the API
- **unittest** — Python's built-in testing framework
- **pytest** — test runner

---

## Project Structure

```
payment_server/
├── src/
│   ├── __init__.py
│   └── create_app.py        # all routes and in-memory logic live here
├── tests/
│   ├── __init__.py
│   └── test_payments.py     # all tests live here
└── README.md
```

---

## Setup

**1. Clone the repo**

```bash
git clone <your-repo-url>
cd payment-server
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
pytest -v
```

You should see all tests passing:

```
tests/test_payments.py::PaymentServerTests::test_create_customer_returns_201 PASSED
tests/test_payments.py::PaymentServerTests::test_create_customer_returns_correct_data PASSED
tests/test_payments.py::PaymentServerTests::test_create_payment_returns_201 PASSED
tests/test_payments.py::PaymentServerTests::test_create_payment_returns_correct_data PASSED
tests/test_payments.py::PaymentServerTests::test_create_refund_returns_201 PASSED
tests/test_payments.py::PaymentServerTests::test_get_customer_by_id_returns_200 PASSED
tests/test_payments.py::PaymentServerTests::test_refund_amount_cannot_exceed_payment_amount PASSED
tests/test_payments.py::PaymentServerTests::test_update_payment_status_returns_200 PASSED
```

---

## API Endpoints

### Customers

| Method | Endpoint       | Description           | Returns   |
| ------ | -------------- | --------------------- | --------- |
| POST   | /customers     | Create a new customer | 201       |
| GET    | /customers/:id | Get a customer by ID  | 200 / 404 |

### Payments

| Method | Endpoint      | Description           | Returns   |
| ------ | ------------- | --------------------- | --------- |
| POST   | /payments     | Create a new payment  | 201       |
| PATCH  | /payments/:id | Update payment status | 200 / 404 |

### Refunds

| Method | Endpoint | Description                       | Returns         |
| ------ | -------- | --------------------------------- | --------------- |
| POST   | /refunds | Create a refund against a payment | 201 / 400 / 404 |

---

## Data Shapes

**Customer**

```json
{
  "id": "cus_174169743284",
  "name": "Alice",
  "email": "alice@gmail.com"
}
```

**Payment**

```json
{
  "id": "pay_174169743299",
  "customer_id": "cus_174169743284",
  "amount": 1000,
  "currency": "usd",
  "status": "pending"
}
```

**Refund**

```json
{
  "id": "ref_174169743310",
  "payment_id": "pay_174169743299",
  "amount": 1000,
  "status": "succeeded"
}
```

---

## Business Rules

- All amounts are integers in cents/pence — 1000 = £10.00 or $10.00
- Payments always start with status `pending`
- Payment status can be updated to `succeeded` or `failed`
- Refunds can only be made against payments that have `succeeded`
- Refund amount cannot exceed the original payment amount

---

## TDD Approach

This project was built strictly test-first. The flow for every single feature was:

```
1. Write a failing test (RED)
2. Write the minimum code to make it pass (GREEN)
3. Clean up the code (REFACTOR)
4. Move to the next test
```

No implementation code was written before a failing test existed for it. The test suite drives the design.

---

## Reflection

Building this project test-first completely changed how I approached writing code. Before TDD, the instinct is to jump straight into writing functions and routes and figure out testing later. Doing it the other way around — writing the test first, watching it fail, then writing just enough code to make it pass — forces you to think clearly about what a feature should actually do before you build it.

The Red-Green cycle also made debugging much easier. When a test fails, you know exactly what broke and why, because each test covers one specific behaviour. The setUp method running before every test meant each test started with a clean slate, so tests never interfered with each other. The biggest lesson from this project is that TDD is not just about testing — it is a design tool that produces cleaner, more focused code.
