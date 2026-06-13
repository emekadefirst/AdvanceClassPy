# unittest is a built-in Python module that provides a framework for writing and running tests. It allows you to create test cases, test suites, and test runners to ensure that your code behaves as expected. Here's an example of how to use unittest to test a simple function:

import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 6), 12)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 6), -12)

import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 6), 8)

#  pytest is a popular testing framework for Python that allows you to write simple and scalable test cases. It provides a more concise and readable syntax compared to unittest. Here's an example of how to use pytest to test the same functions:

import pytest

def divide(a, e):
    if e == 0:
        raise ValueError("Cannot divide by zero")
    return a/e

def test_divide():
    assert(divide(10, 2) == 5)

import pytest

def subtract(a, b):
    return a - b

def test_subtract():
    assert(subtract(10, 5) == 5)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

