def fibonacci(number):
    previous_n = 0
    current_n = 1

    if number == 0:
        return previous_n
    elif number == 1:
        return current_n
    else:
        for i in range(1, number):
            next_n = previous_n + current_n
            previous_n = current_n
            current_n = next_n
        return current_n

import unittest

expected_inputs_outputs = [(0, 0), (1, 1), (2, 1), (12, 144), (13, 233)] # Known fibonacci numbers and their position (position, fibonacci_number)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        for position, fibonacci_number in expected_inputs_outputs:
            with self.subTest(position=position, fibonacci_number=fibonacci_number):
                self.assertEqual(fibonacci(position), fibonacci_number)

if __name__ == '__main__':
    try:
        number = input("Enter a positive integer: ")
        number = int(number)
        if number > 0:
            print(fibonacci(number))
        else:
            raise Exception
    except:
        print("Try again, not a positive integer")
