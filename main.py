class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}" 
    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.quantity}', '{self.unit}')"
    def __eq__(self, other):
        if other.name==self.name and other.unit==self.unit:
            return True
        return False