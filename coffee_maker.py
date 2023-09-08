class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"\n{'-' * 40}")
        print(f"{' ' * 17}REPORT{' ' * 17}")
        print(f"{'-' * 40}")
        print(f"Water : {self.resources['water']}ml")
        print(f"Milk  : {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\n{'-' * 35}")
                print(f"Sorry, there is NOT enough {item}.")
                print(f"{'-' * 35}")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\nEnjoy your {order.name}☕")
        print(f"{'~' * 55}")
