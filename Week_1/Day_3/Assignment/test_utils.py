import unittest
from utils import *

class TestUtils(unittest.TestCase):
    # Matcher Group 1: Exact Equality Tests
    # These tests check if the function returns the exact expected output for given inputs.

    # 1. assertEqual
    def test_sum_numbers(self):
        result = sum_numbers(2, 3)
        self.assertEqual(result, 5)

    # 2. assertDictEqual
    def test_create_user(self):
        user = create_user("Elsa", 23)
        expected_user = {
            "name": "Elsa",
            "age": 23,
            "created_at": user["created_at"]  # We can't predict the exact timestamp
        }
        self.assertDictEqual(user, expected_user)

    # 3. assertListEqual
    def test_filter_adults(self):
        users = [
            {"name": "Bethel", "age": 3},
            {"name": "Arnold", "age": 18},
            {"name": "Charlie", "age": 20},
            {"name": "Julie", "age": 39}
        ]
        adults = filter_adults(users)
        expected_adults = [
            {"name": "Arnold", "age": 18},
            {"name": "Charlie", "age": 20},
            {"name": "Julie", "age": 39}
        ]
        self.assertListEqual(adults, expected_adults)

    # 4. assertIs
    def test_identity(self):
        result = sum_numbers(2, 3)
        self.assertIs(result, 5)

    # Failing tests for exact equality
    def test_exact_equality_failures(self):
        # 1. assertEqual 
        self.assertEqual(sum_numbers(2, 2), 5)

        # 2. assertDictEqual 
        user = create_user("Elsa", 23)
        wrong_user = {"name": "Elsa", "age": 22, "created_at": user["created_at"]}
        self.assertDictEqual(user, wrong_user)

        # 3. assertListEqual 
        users = [
            {"name": "Bethel", "age": 3},
            {"name": "Arnold", "age": 18},
            {"name": "Charlie", "age": 20}
        ]
        adults = filter_adults(users)
        wrong_adults = [{"name": "Arnold", "age": 18}]  # missing Charlie
        self.assertListEqual(adults, wrong_adults)

        # 4. assertIs
        result = sum_numbers(2, 3)
        self.assertIs(result, 6)

    # Matcher Group 2: Negation Assertions (.not)
    # These check that something is NOt true.

    def test_negation_assertions(self):
        # 1. assertNotEqual
        self.assertNotEqual(sum_numbers(1, 1), 3)

        # 2. assertIsNot
        self.assertIsNot(None, 0)

        # 3, assertNotIn
        self.assertNotIn(5, [1, 2, 3, 4])

    # Failing tests for negation assertions
    def test_negation_failures(self):
        # 1. assertNotEqual 
        self.assertNotEqual(sum_numbers(2, 2), 4)

        # 2. assertIsNot 
        self.assertIsNot(5, 5)

        # 3. assertNotIn 
        self.assertNotIn("Arnold", ["Bethel", "Arnold", "Charlie"])

    # Matcher Group 3: Truthiness Assertions
    # These check if a value is True, False, None, or Not None.

    def test_truthiness_assertions(self):
        # 1. assertTrue
        self.assertTrue(find_in_list([1, 2, 3], 2))

        # 2. assertFalse
        self.assertFalse(find_in_list([1, 2, 3], 4))

        # 3. assertIsNone
        value = None
        self.assertIsNone(value)

        # 4. assertIsNotNone
        self.assertIsNotNone(create_user("Kellie", 26))

    # Failing tests for truthiness assertions
    def test_truthiness_failures(self):
        # 1. assertTrue 
        self.assertTrue(find_in_list([1, 2, 3], 4))

        # 2. assertFalse 
        self.assertFalse(find_in_list([1, 2, 3], 2))

        # 3. assertIsNone 
        value = "Not None"
        self.assertIsNone(value)

        # 4. assertIsNotNone 
        self.assertIsNotNone(None)

    # Matcher Group 4: Number Matchers
    # These check if a number is greater than, greater than or equal to, less than, less than or equal to, or approximately equal to another

    def test_number_matchers(self):
        # 1. assertGreater
        self.assertGreater(sum_numbers(2, 3), 4)

        # 2. assertGreaterEqual
        self.assertGreaterEqual(sum_numbers(2, 3), 5)

        # 3. assertLess
        self.assertLess(approximate_division(10, 2), 6)

        # 4. assertLessEqual
        self.assertLessEqual(approximate_division(10, 2), 5)

        # 5. assertAlmostEqual
        self.assertAlmostEqual(approximate_division(10, 3), 3.33, places=2)

    # Failing tests for number matchers
    def test_number_matchers_failures(self):
        # 1. assertGreater 
        self.assertGreater(sum_numbers(2, 3), 5)

        # 2. assertGreaterEqual 
        self.assertGreaterEqual(sum_numbers(2, 3), 6)

        # 3. assertLess 
        self.assertLess(approximate_division(10, 2), 5)

        # 4. assertLessEqual 
        self.assertLessEqual(approximate_division(10, 2), 4)

        # 5. assertAlmostEqual 
        self.assertAlmostEqual(approximate_division(10, 3), 3.34, places=2)

    # Matcher Group 5: String Matchers
    # These are used to check patterns inside strings using regular expressions (regex).

    def test_string_matchers(self):
        # 1. assertRegex
        self.assertRegex("Hello, World!", r"Hello")

        # 2. assertNotRegex
        self.assertNotRegex("Hello, World!", r"Python")

    # Failing tests for string matchers
    def test_string_matchers_failures(self):
        # 1. assertRegex 
        self.assertRegex("Hello, World!", r"Python")

        # 2. assertNotRegex 
        self.assertNotRegex("Hello, World!", r"Hello")

    # Matcher Group 6: Arrays/Iterables
    #This group checks whether an item exists inside a collection like lists, arrays, strings, tuples

    def test_arrays_iterables(self):
        users = ["Bethel", "Arnold", "Charlie", "Julie"]
        # 1. assertIn
        self.assertIn("Arnold", users)

        # 2. assertNotIn
        self.assertNotIn("David", users)

    # Failing tests for arrays/iterables
    def test_arrays_iterables_failures(self):
        users = ["Bethel", "Arnold", "Charlie", "Julie"]
        # 1. assertIn (will fail)
        self.assertIn("David", users)

        # 2. assertNotIn (will fail)
        self.assertNotIn("Arnold", users)

    # Matcher Group 7: Exceptions
    # This group checks that a function raises an error when something invalid happens.

    def test_exceptions(self):
        # 1. assertRaises
        with self.assertRaises(ValueError):
            parse_json("")  # This should raise a ValueError because the input is empty

        # 2. assertRaisesRegex
        with self.assertRaisesRegex(ValueError, "No JSON string provided"):
            parse_json("")  # This should raise a ValueError with the specific message

    # Failing tests for exceptions
    def test_exceptions_failures(self):
        # assertRaises fails if no error is raised
        with self.assertRaises(ValueError):
            sum_numbers(2, 3)  # no error, test will fail

        # assertRaisesRegex fails if message doesn't match
        with self.assertRaisesRegex(ValueError, "Wrong message"):
            parse_json("")  # error exists but message does not match


if __name__ == '__main__':
    unittest.main()