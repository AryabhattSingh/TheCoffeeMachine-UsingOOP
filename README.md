# TheCoffeeMachine-UsingOOP

This is a simple interactive coffee machine program that allows users to select and purchase coffee drinks. The program also includes hidden features for machine attendants to check ingredient quantities and turn off the machine.
`This project is made by leveraging OOP in Python`.

## Features

1. **Coffee Mug ASCII Art:** The program displays a beautiful coffee mug in ASCII art to create an inviting atmosphere.
   ```shell
         )  (
        (   ) )
         ) ( (
        __)__(_)_
     .-'---------|  
    ( C|/\/\/\/\/|
     '-./\/\/\/\/|
       '_________'
        '-------'
   ```

3. **Coffee Menu:** A list of coffee drinks is presented to the user, allowing them to choose from available options. The options are
   ```shell
   What would you like?
   Type '1' for Espresso
   Type '2' for Latte
   Type '3' for Cappuccino
   ```

4. **User Input Validation:** Users are prompted to select a drink by typing `'1', '2', or '3'`. If the user inputs an invalid value, such as a non-numeric character or a number outside the valid range, a caution message is displayed, and the machine requests another selection.

5. **Ingredient Availability Check:** The machine internally checks if it has all the required ingredients in sufficient quantity to prepare the selected drink.

6. **Coin Insertion:** If the required ingredients are available, the user is prompted to insert coins. The machine asks the user to input the number of `Quarters`, `Dimes`, `Nickels`, and `Pennies` they are inserting.

7. **Coin Input Validation:** The program ensures that the user's coin inputs are valid, including checking for non-numeric values, negative values, or decimal values. If any invalid input is detected, a warning message is displayed, and the user is asked to provide the correct value.

8. **Total Money Calculation:** The machine calculates the total value of the money inserted by the user based on the quantity of each coin denomination.

9. **Cost Comparison:** After calculating the total money inserted, the program compares it to the cost of the user-selected drink.

10. **Drink Preparation:** If the money inserted is greater than or equal to the drink's cost, the machine prepares the selected drink and returns any change to the user after deducting the cost.

11. **Ingredient Quantity Report (Hidden Feature I):** Machine attendants can type `report` to view the quantity of each ingredient (`water, milk, coffee`) currently available in the machine.

12. **Machine Shutdown (Hidden Feature II):** Machine attendants can turn off the machine by typing `off`.

## Getting Started

To run the coffee machine program, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/AryabhattSingh/TheCoffeeMachine-UsingOOP.git
   ```

2. Navigate to the project directory:

   ```
   cd TheCoffeeMachine-UsingOOP
   ```

3. Run the program:

   ```
   python main.py
   ```

## Usage

1. When prompted, type '1', '2', or '3' to select a coffee drink from the menu.
2. Follow the instructions to insert coins. Make sure to provide valid coin quantities.
3. If you want to check the quantity of ingredients, type 'report' (Hidden Feature I).
4. To turn off the machine, type 'off' (Hidden Feature II).

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ASCII art for the coffee mug was inspired by [ASCII Art Archive](https://www.asciiart.eu/).
- Special thanks to our contributors for their valuable input and support.

Enjoy your coffee! ☕️
