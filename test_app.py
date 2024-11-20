"""
Module de tests pour le module app.
"""

import unittest
from app import multiplication

class TestApp(unittest.TestCase):
    """Classe contenant les tests pour la fonction multiplication."""
    
    def test_multiplication_true(self):
        """
        Teste si la multiplication retourne le résultat attendu.
        """
        self.assertEqual(multiplication(2, 3), 6)

    def test_multiplication_not_true(self):
        """
        Teste si la multiplication ne retourne pas un résultat incorrect.
        """
        self.assertNotEqual(multiplication(2, 3), 5)

if __name__ == "__main__":
    unittest.main()