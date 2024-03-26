import unittest
from vala1tokenizer import VALa1Tokenizer

class TestVALa1Tokenizer(unittest.TestCase):
    def test_tokenize(self):
        tokenizer = VALa1Tokenizer()
        text = "This is a test sentence."
        expected_tokens = ["This", "is", "a", "test", "sentence", "."]
        self.assertEqual(tokenizer.tokenize(text), expected_tokens)

if __name__ == '__main__':
    unittest.main()
  
