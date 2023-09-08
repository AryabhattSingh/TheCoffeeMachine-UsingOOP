from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from ascii_art import logo


def get_coffee_name(user_choice):
    """A static method which returns the name of the coffee drink based on the user's integer input"""
    if user_choice == "1":
        return "latte"
    elif user_choice == "2":
        return "espresso"
    else:
        return "cappuccino"


coffee_machine_ON = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print(logo)

while coffee_machine_ON:
    user_input = input(f"\nWhat would you like?\n{menu.get_items()}"
                       "\nEnter your choice :").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
        print(f"{'-' * 40}")
    elif user_input == "off":
        coffee_machine_ON = False
    elif user_input in ["1", "2", "3"]:

        coffee_name = get_coffee_name(user_input)
        drink = menu.find_drink(coffee_name)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print(f"\n{'+' * 40}")
        print("Kindly enter a valid input")
        print(f"{'+' * 40}")
