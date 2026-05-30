class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}" 