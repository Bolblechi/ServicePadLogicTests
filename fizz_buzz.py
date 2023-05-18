def fizz_buzz(number):
    result = number
    if number % 15 == 0:
        result = "fizz buzz"
    else:
        if number % 5 == 0:
            result = "buzz"
        if number % 3 == 0:
            result = "fizz"
    return result

import unittest
import random

prime_numbers = [1, 2, 7, 11, 13]# Using prime numbers, except 3 and 5, to ensure that aren't multiples of them

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        '''
        Any number multiplied by 3 is a multiple of 3 so we ensure be testing
        the desired behavior.
        '''
        for number in prime_numbers:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number * 3), "fizz")

    def test_buzz(self):
        '''
        Any number multiplied by 5 is a multiple of 5 so we ensure be testing
        the desired behavior.
        '''
        for number in prime_numbers:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number * 5), "buzz")

    def test_fizz_buzz(self):
        '''
        Any number multiplied by 15 is a multiple of both, 5 and 3, so we
        ensure be testing the desired behavior. The range to ensure the number
        falls inside the problem description
        '''
        for number in range(1, 7):
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number * 15), "fizz buzz")

    def test_number(self):
        for number in prime_numbers:
            with self.subTest(number=number):
                self.assertEqual(fizz_buzz(number), number)

if __name__ == '__main__':
    for number in range(1, 101):
        print(fizz_buzz(number))
