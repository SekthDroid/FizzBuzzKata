from unittest import TestCase
from fizzbuzz.fizzbuzz import FizzBuzz

__author__ = 'SekthDroid'


class FizzBuzzTest(TestCase):

    def setUp(self):
        super().setUp()
        self.fizzbuzz = FizzBuzz()

    def test_should_return_number_when_not_divisible_by_three_or_five(self):
        self.assertEqual(1, self.fizzbuzz.execute(1))
        self.assertEqual(2, self.fizzbuzz.execute(2))
        self.assertEqual(4, self.fizzbuzz.execute(4))

    def test_should_return_fizz_when_number_is_divisible_by_three(self):
        self.assertEqual("fizz", self.fizzbuzz.execute(3))
        self.assertEqual("fizz", self.fizzbuzz.execute(9))

    def test_should_return_buzz_when_number_is_divisible_by_five(self):
        self.assertEqual("buzz", self.fizzbuzz.execute(5))
        self.assertEqual("buzz", self.fizzbuzz.execute(10))

    def test_should_return_fizzbuzz_when_number_is_divisible_by_three_and_five(self):
        self.assertEqual("fizzbuzz", self.fizzbuzz.execute(15))
        self.assertEqual("fizzbuzz", self.fizzbuzz.execute(30))

    def test_should_return_pop_when_number_is_divisible_by_seven(self):
        self.assertEqual("pop", self.fizzbuzz.execute(7))

    def test_should_return_fizzpop_when_number_is_divisible_by_three_and_seven(self):
        self.assertEqual("fizzpop", self.fizzbuzz.execute(21))

    def test_should_return_buzz_pop_when_number_is_divisible_by_five_and_seven(self):
        self.assertEqual("buzzpop", self.fizzbuzz.execute(35))