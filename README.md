# Simple Coffee Machine

The Simple Coffee Machine project is a text-based simulation of a coffee vending machine. Users can order espresso, latte, or cappuccino, and the machine will check if there are enough resources (water, milk, coffee) to make the drink. If the resources are sufficient, the machine will process the payment, dispense the coffee, and update the resources. It also provides the option to view a report of the current resources and earnings.

**Features:**
- **Coffee Options:** The user can choose between espresso, latte, and cappuccino.
- **Resource Management:** The machine checks if there are sufficient ingredients before preparing the coffee. If resources are insufficient, it informs the user.
- **Payment Processing:** The machine calculates the total amount from inserted coins and checks if it meets the drink's cost. If the payment is insufficient, it refunds the money.
- **Change Handling:** If the user inserts more money than required, the machine provides change.
- **Reports:** Users can view the current resource levels and the total profit by typing "report."
- **Turn Off Option:** The machine can be turned off by entering "off" as a command.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### How to Use

1. Clone or download the repository to your local machine.
2. Run the script using Python:

   ```bash
   python simple_coffee_machine.py
   ```

3. Follow the on-screen prompts to:
   - Choose a coffee option (espresso, latte, cappuccino).
   - Insert coins to make a purchase.
   - View reports on the machine's resources and earnings.
   - Turn off the machine by typing "off."

4. The machine will check if there are sufficient resources to make the coffee. If yes, it will process the payment and serve the coffee, handling any necessary change.

### Customization

You can customize the Simple Coffee Machine by:
- **Adding More Drinks:** Modify the `MENU` dictionary to include additional coffee types or other beverages.
- **Adjusting Prices and Resources:** Change the prices or required resources for each drink to simulate different machine configurations.
- **Enhancing Functionality:** Add features such as restocking resources, handling alternative payment methods, or adding new report metrics.
