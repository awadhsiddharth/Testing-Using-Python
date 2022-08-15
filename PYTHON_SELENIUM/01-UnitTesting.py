import unittest

class TestDemo(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_add(self):
        self.assertEqual(12 + 20, 50)

    def test_isUpper(self):
        self.assertEqual("Vladimir Putin".upper(), "HELLo")

if __name__ == '__main__':
    unittest.main()
