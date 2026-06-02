import pytest
from recipes import *

class TestIngredient:
    def test_ingredient(self):
        ingredient = Ingredient("Молоко", 250.0, "мл")
        assert ingredient.name == "Молоко"
        assert ingredient.amount == 250.0
        assert ingredient.unit == "мл"