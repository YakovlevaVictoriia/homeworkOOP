class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self._quantity = 0.0
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}" 

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if other.name==self.name and other.unit==self.unit:
            return True
        return False

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = []
        for elem in ingredients:
            self.add_ingredient(elem)

    def add_ingredient(self, ingredient: Ingredient):
        flag = True
        for elem in self.ingredients:
            if elem==ingredient:
                elem.quantity+=ingredient.quantity
                flag = False
        if flag == True:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            if float(ratio)>0:
                return True
            else:
                return False
        except Exception:
            return False

    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio):
            new_ingredients=[]
            for elem in self.ingredients:
                new_ingredients.append(Ingredient(elem.name, elem.quantity*ratio, elem.unit))
            return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        res = f"Чтобы приготовить {self.title} нужно:\n"
        for i in self.ingredients:
            res += f"{i} \n"
        return res

class ShoppingList:
    def __init__(self):
        self._items = []
    
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        new_recipe=recipe.scale(portions)
        for elem in new_recipe.ingredients:
            self._items.append((elem,recipe.title))
