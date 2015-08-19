from unittest import TestCase
from fizzbuzz.fizzbuzz import FizzBuzz

__author__ = 'SekthDroid'


class FizzBuzzTest(TestCase):

    def test_should_return_number_when_not_divisible_by_three_or_five(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(1, fizzbuzz.execute(1))
        self.assertEqual(2, fizzbuzz.execute(2))
        self.assertEqual(4, fizzbuzz.execute(4))