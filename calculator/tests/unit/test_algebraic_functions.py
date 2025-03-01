import os
import sys
import pytest

# Ajoute le dossier racine au Python Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils import add, subtract, multiply, divide

class TestCalculator:

    def test_addition(self):
        assert 4 == add(2, 2)

    def test_subtraction(self):
        assert 2 == subtract(4, 2)

    def test_multiplication(self):
        assert 9 == multiply(3, 3)

    def test_division(self):
        assert 2 == divide(4, 2)

    def test_division_by_zero(self):
        with pytest.raises(ValueError):
            divide(4, 0)
