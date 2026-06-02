import pytest
from main import Ingredient, Recipe, ShoppingList

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

    def test_add_ingredient(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe = Recipe("Блины", [ingredient1])
        recipe.add_ingredient(ingredient2)
        assert recipe.ingredients == [ingredient1, ingredient2]

        recipe.add_ingredient(ingredient1)
        assert recipe.ingredients == [Ingredient("Молоко", 500.0, "мл"), ingredient2]

    def test_scale(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe = Recipe("Блины", [ingredient1, ingredient2])
        scaled_recipe = recipe.scale(2)
        assert scaled_recipe is not recipe
        assert scaled_recipe.title == "Блины"
        assert scaled_recipe.ingredients == [Ingredient("Молоко", 500.0, "мл"), Ingredient("Мука", 200.0, "г")]
        with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
            recipe.scale(-1)
    
    def test_len(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe = Recipe("Блины", [ingredient1, ingredient2])
        assert len(recipe) == 2

class TestShoppingList:
    def test_add_recipe(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe = Recipe("Блины", [ingredient1, ingredient2])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe,3)
        assert shopping_list._items == [(Ingredient("Молоко", 750.0, "мл"),"Блины"), (Ingredient("Мука", 300.0, "г"),"Блины")]
        with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
            shopping_list.add_recipe(recipe,-1)

    def test_remove_recipe(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe1 = Recipe("Блины", [ingredient1, ingredient2])
        recipe2 = Recipe("Панкейки", [ingredient1])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe1,3)
        shopping_list.add_recipe(recipe2,2)
        shopping_list.remove_recipe("Блины")
        assert shopping_list._items == [(Ingredient("Молоко", 500.0, "мл"),"Панкейки")]

    def test_get_list(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe1 = Recipe("Блины", [ingredient1, ingredient2])
        recipe2 = Recipe("Панкейки", [ingredient1])
        shopping_list = ShoppingList()
        shopping_list.add_recipe(recipe1,3)
        shopping_list.add_recipe(recipe2,2)
        assert shopping_list.get_list() == [(Ingredient("Молоко", 1250.0, "мл")), (Ingredient("Мука", 300.0, "г"))]

    def test_add(self):
        ingredient1 = Ingredient("Молоко", 250.0, "мл")
        ingredient2 = Ingredient("Мука", 100.0, "г")
        recipe1 = Recipe("Блины", [ingredient1, ingredient2])
        recipe2 = Recipe("Панкейки", [ingredient1])
        shopping_list1 = ShoppingList()
        shopping_list2 = ShoppingList()
        shopping_list1.add_recipe(recipe1,3)
        shopping_list2.add_recipe(recipe2,2)
        new_shopping_list=shopping_list1+shopping_list2
        assert new_shopping_list.get_list() ==  [(Ingredient("Молоко", 1250.0, "мл")), (Ingredient("Мука", 300.0, "г"))]
