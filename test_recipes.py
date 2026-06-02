import pytest
from recipes import *

class TestIngredient:
    def test_ingredient(self):
        ingredient = Ingredient("Молоко", 250.0, "мл")
        assert ingredient.name == "Молоко"
        assert ingredient.amount == 250.0
        assert ingredient.unit == "мл"
    
    def test_quantity_negative_amount(self):
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Молоко", -250.0, "мл")
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Молоко", 0.0, "мл")

    def test_str(self):
        ingredient = Ingredient("Молоко", 250.0, "мл")
        assert str(ingredient) == "Молоко: 250.0 мл"