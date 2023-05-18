import re

def counting_words(sentence):
    words = re.findall("\d+|[a-zA-Z]+'?[a-zA-Z]+", sentence) # Including only alphanumeric characters and words with apostrophe
    words_and_repetitions = {}

    for word in words:
        word = word.lower()
        if words_and_repetitions.get(word):
            words_and_repetitions[word] += 1
        else:
            words_and_repetitions[word] = 1
    return words_and_repetitions

import unittest
import random

class TestCountingWords(unittest.TestCase):
    def test_words(self):
        word = "sentence"
        number_of_repetitions = random.randint(1, 100)
        result = counting_words(f'{word} ' * number_of_repetitions)
        self.assertEqual(result[word], number_of_repetitions)

    def test_numbers(self):
        word = "7"
        number_of_repetitions = random.randint(1, 100)
        result = counting_words(f'{word} ' * number_of_repetitions)
        self.assertEqual(result[word], number_of_repetitions)

    def test_words_and_numbers(self):
        word = "sentence"
        number = "7"
        number_of_repetitions = random.randint(1, 100)
        result = counting_words(f'{word} {number} ' * number_of_repetitions)
        self.assertEqual(result[word], number_of_repetitions)
        self.assertEqual(result[number], number_of_repetitions)

    def test_words_with_apostrophe(self):
        word = "you're"
        number_of_repetitions = random.randint(1, 100)
        result = counting_words(f'{word} ' * number_of_repetitions)
        self.assertEqual(result[word], number_of_repetitions)

if __name__ == '__main__':
    print(counting_words("Hi how are things? How are you? Are you a developer? I am also a developer"))
