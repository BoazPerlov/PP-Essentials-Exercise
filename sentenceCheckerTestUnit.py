import unittest
from validSentenceChecker import sentenceChecker

#using the unittest library, we create a subclass of its TestCase class to check several example of valid and invalid sentences
class TestChecker(unittest.TestCase):

    def test_sentence(self):
        self.assertTrue(sentenceChecker('The quick brown fox said “hello Mr lazy dog”.'))
        self.assertTrue(sentenceChecker('The quick brown fox said hello Mr lazy dog.'))
        self.assertTrue(sentenceChecker('One lazy dog is too few, 13 is too many.'))
        self.assertTrue(sentenceChecker('One lazy dog is too few, thirteen is too many.'))
        self.assertTrue(sentenceChecker('How many "lazy dogs" are there?'))
        self.assertFalse(sentenceChecker('The quick brown fox said "hello Mr. lazy dog".'))
        self.assertFalse(sentenceChecker('the quick brown fox said “hello Mr lazy dog".'))
        self.assertFalse(sentenceChecker('"The quick brown fox said “hello Mr lazy dog."'))
        self.assertFalse(sentenceChecker('One lazy dog is too few, 12 is too many.'))
        self.assertFalse(sentenceChecker('Are there 11, 12, or 13 lazy dogs?'))
        self.assertFalse(sentenceChecker('There is no punctuation in this sentence'))
        self.assertFalse(sentenceChecker('boaz enjoyed this challenge!'))
        self.assertTrue(sentenceChecker('Boaz enjoyed "this" challenge!'))
        self.assertFalse(sentenceChecker(r'123456%%^^^%%%%!'))
        self.assertFalse(sentenceChecker('Boaz ""enjoyed" this challenge!'))


if __name__ == "__main__":
    unittest.main()
