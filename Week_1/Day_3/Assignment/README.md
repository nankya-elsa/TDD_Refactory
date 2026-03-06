# Python Utility Module Testing

This project demonstrates unit testing of a small Python utility module (`utils.py`) using Python's `unittest` framework. The tests are designed to cover equivalents of common Jest matchers in Python.

---

## Matcher Reference Table

| Jest Matcher       | Python Equivalent (unittest)                              |
| ------------------ | --------------------------------------------------------- |
| `toBe`             | `assertIs` / `assertEqual`                                |
| `toEqual`          | `assertEqual`                                             |
| `toStrictEqual`    | `assertDictEqual` / `assertListEqual`                     |
| `.not`             | `assertNotEqual` / `assertIsNot` / `assertNotIn`          |
| `toBeNull`         | `assertIsNone`                                            |
| `toBeTruthy`       | `assertTrue`                                              |
| `toBeFalsy`        | `assertFalse`                                             |
| Number comparisons | `assertGreater` / `assertLessEqual` / `assertAlmostEqual` |
| `toMatch`          | `assertRegex` / `assertNotRegex`                          |
| `toContain`        | `assertIn` / `assertNotIn`                                |
| `toThrow`          | `assertRaises` / `assertRaisesRegex`                      |

---

## Test Structure

All tests are written inside `test_utils.py` using `unittest.TestCase`. Each matcher group has tests demonstrating both **passing** and **failing** scenarios to ensure understanding of test behavior.

---

## Matcher Group 1: Exact Equality

Checks that a function returns the exact expected value, dictionary, or list.

```python
# assertEqual
self.assertEqual(sum_numbers(2, 3), 5)

# assertDictEqual
user = create_user("Elsa", 23)
expected_user = {"name": "Elsa", "age": 23, "created_at": user["created_at"]}
self.assertDictEqual(user, expected_user)

# assertListEqual
users = [{"name":"Bethel","age":3}, {"name":"Arnold","age":18}]
adults = filter_adults(users)
expected_adults = [{"name":"Arnold","age":18}]
self.assertListEqual(adults, expected_adults)

# assertIs
result = sum_numbers(2, 3)
self.assertIs(result, 5)
```

---

## Matcher Group 2: Negation Assertions (`.not`)

Checks that something does not equal, is not the same object, or is not in a collection.

```python
# assertNotEqual
self.assertNotEqual(sum_numbers(1, 1), 3)

# assertIsNot
self.assertIsNot(None, 0)

# assertNotIn
self.assertNotIn(5, [1, 2, 3, 4])
```

---

## Matcher Group 3: Truthiness Assertions

Tests whether a value is `True`, `False`, `None`, or Not `None`.

```python
# assertTrue
self.assertTrue(find_in_list([1,2,3], 2))

# assertFalse
self.assertFalse(find_in_list([1,2,3], 4))

# assertIsNone
value = None
self.assertIsNone(value)

# assertIsNotNone
self.assertIsNotNone(create_user("Kellie", 26))
```

---

## Matcher Group 4: Number Matchers

Compares numeric values.

```python
# assertGreater
self.assertGreater(sum_numbers(2, 3), 4)

# assertGreaterEqual
self.assertGreaterEqual(sum_numbers(2, 3), 5)

# assertLess
self.assertLess(approximate_division(10, 2), 6)

# assertLessEqual
self.assertLessEqual(approximate_division(10, 2), 5)

# assertAlmostEqual
self.assertAlmostEqual(approximate_division(10, 3), 3.33, places=2)
```

---

## Matcher Group 5: String Matchers

Uses regular expressions to check string patterns.

```python
# assertRegex
self.assertRegex("Hello, World!", r"Hello")

# assertNotRegex
self.assertNotRegex("Hello, World!", r"Python")
```

---

## Matcher Group 6: Arrays / Iterables

Checks whether an item exists in a collection.

```python
# assertIn
users = ["Bethel", "Arnold", "Charlie"]
self.assertIn("Arnold", users)

# assertNotIn
self.assertNotIn("David", users)
```

---

## Matcher Group 7: Exceptions

Ensures functions raise expected errors.

```python
# assertRaises
with self.assertRaises(ValueError):
    parse_json("")

# assertRaisesRegex
with self.assertRaisesRegex(ValueError, "No JSON string provided"):
    parse_json("")
```

---

## Notes

- **Failing Tests:** Each matcher group in `test_utils.py` also includes failing tests to illustrate what happens when expectations are not met.
- **`datetime.now()` Handling:** When testing functions that return timestamps, use the actual value returned to compare, as shown in `assertDictEqual` for `create_user()`. This avoids timing mismatches.
- **Test Execution:** Run the tests with:

```bash
python -m unittest test_utils.py
```
