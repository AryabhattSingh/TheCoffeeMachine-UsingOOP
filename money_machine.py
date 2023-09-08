import os

import ascii_art


def clear_console():
    os.system('cls')


class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money : {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("\nPlease insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            clear_console()
            print(ascii_art.logo)
            print(f"\n{'~' * 55}")
            print(f"Here is {self.CURRENCY}{change} in change. Please collect cash.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"\n{'+' * 46}")
            print("Sorry that's not enough money. Money refunded.")
            print(f"{'+' * 46}")
            self.money_received = 0
            return False

