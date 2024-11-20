"""
Module contenant une fonction de multiplication.
"""

def multiplication(valeur, multiplicateur):
    """
    Multiplie deux nombres.

    Args:
        valeur (int, float): Le premier nombre.
        multiplicateur (int, float): Le deuxième nombre.

    Returns:
        int, float: Le résultat de la multiplication.
    """
    return valeur * multiplicateur

if __name__ == "__main__":
    print(multiplication(2, 5))
