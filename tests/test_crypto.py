# tests/test_crypto.py
import unittest
from src.crypto_utils import sToN, nToS

class TestCrypto(unittest.TestCase):

    def test_ston_ntos(self):
        original = "hello world"
        n = sToN(original)
        result = nToS(n)
        self.assertEqual(original, result)

if __name__ == '__main__':
    unittest.main()
