import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_multiplicationTrue(self):
        self.assertEqual(app.multiply(2, 3), 6)

    def test_multiplicationNotTrue(self):
        self.assertNotEqual(app.multiply(2, 3), 5)

if __name__ == '__main__':
    unittest.main()