import pytest
from main import Ingredient, Recipe, ShoppingList, DietaryRecipe

class TestIngredient:
    def test_ingredient(self):
        ingredient = Ingredient("Молоко", 250.0, "мл")
        assert ingredient.name == "Молоко"
        assert ingredient.quantity == 250.0
        assert ingredient.unit == "мл"
    
    def test_quantity_negative_amount(self):
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Молоко", -250.0, "мл")
        with pytest.raises(ValueError, match="Количество должно быть положительным"):
            Ingredient("Молоко", 0.0, "мл")

    def test_str(self):
        ingredient = Ingredient("Молоко", 250.0, "мл")
        assert str(ingredient) == "Молоко: 250.0 мл"
    
    def test_eq(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Молоко", 750.0, "мл")
        ingredient3 = Ingredient("Молоко", 250.0, "л")
        ingredient4 = Ingredient("Вода", 250.0, "мл")
        assert ingredient1 == ingredient2
        assert ingredient1 != ingredient3
        assert ingredient1 != ingredient4

class TestRecipe:
    def test_recipe(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe = Recipe("Блины", [ingredient1, ingredient2])
        assert recipe.title == "Блины"
        assert recipe.ingredients == [ingredient1, ingredient2]