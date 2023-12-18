# Creates a function to get user choice for 'Drinks' or 'Snacks'
def get_user_option():
    option = input("Enter 'Drinks' for drinks or 'Snacks' for snacks: ")
    while option not in ['Drinks', 'Snacks']:
        option = input("Invalid input. Please enter 'Drinks' for drinks or 'Snacks' for snacks: ")
    return option

# Creates a function to calculate change received when depositing money
def calculating_change(cash_deposited, price):
    change = cash_deposited - price
    while change < 0:
        cash_deposited = float(input("Insufficient cash. Please enter a larger amount: "))
        change = cash_deposited - price
    return cash_deposited, change

# Main function for the vending machine
def vending_machine():
    while True:  # Uses while for infinite loop to keep the vending machine running
        try:
            # Displays the vending machine menu
            print("""d888888P                            d8             dP     dP                         dP oo                      8888ba.88ba                    dP       oo                   
   88                               88             88     88                         88                         88  `8b  `8b                   88                            
   88    .d8888b. 88d888b. .d8888b. .P .d8888b.    88    .8P .d8888b. 88d888b. .d888b88 dP 88d888b. .d8888b.    88   88   88 .d8888b. .d8888b. 88d888b. dP 88d888b. .d8888b. 
   88    88ooood8 88'  `88 88'  `88    Y8ooooo.    88    d8' 88ooood8 88'  `88 88'  `88 88 88'  `88 88'  `88    88   88   88 88'  `88 88'  `"" 88'  `88 88 88'  `88 88ooood8 
   88    88.  ... 88       88.  .88          88    88  .d8P  88.  ... 88    88 88.  .88 88 88    88 88.  .88    88   88   88 88.  .88 88.  ... 88    88 88 88    88 88.  ... 
   dP    `88888P' dP       `88888P'    `88888P'    888888'   `88888P' dP    dP `88888P8 dP dP    dP `8888P88    dP   dP   dP `88888P8 `88888P' dP    dP dP dP    dP `88888P' 
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~.88~oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                                                                                     d8888P                                                                  
""")
            print("Available items:")
            print("Drinks: (D1) Coke ($1.00), (D2) Pepsi ($1.00), (D3) Water ($0.75), (D4) Prime ($5.45), (D5) Watermelon Juice ($1.00)")
            print("Snacks: (S1) Lays ($1.50), (S2) Snickers Bar ($1.00), (S3) Nuts ($1.75), (D4) Cadburry ($1.25), (D5) Skittles ($1.00)")
            
            # Get user choice for 'Drinks' or 'Snacks'
            option = get_user_option()

            # Dictionary containing item prices for 'Drinks' and 'Snacks'
            item_prices = {'Drinks': {'Coke': 1.00, 'Pepsi': 1.00, 'Water': 0.75, 'Prime': 5.45, 'Watermelon Juice': 1.00},
                           'Snacks': {'Lays': 1.50, 'Chocolate Bar': 1.00, 'Nuts': 1.75, 'Cadburry': 1.25, 'Skittles': 1.00}, }

            # Get user's chosen item
            print("\nChoose your item:")
            item = input(f"Available items: {', '.join(item_prices[option].keys())}: ")
            while item not in item_prices[option].keys():
                item = input(f"Invalid input. Please enter the name of the item: ")

            # Get cash from the user and calculate change also using float to create decimal for change allowing for precise change calculation
            cash_deposited = float(input(f"Please enter the cash amount for {item} (${item_prices[option][item]}): "))
            cash_deposited, change = calculating_change(cash_deposited, item_prices[option][item])

            # Display the purchased item and change as well as a thank you message
            print(f"\nHere is your {item}. Thank you for your purchase valued customer! Come again :)")
            print(f"Change: ${change:.2f}")
            # Uses the * symbol to print a line creating a border line
            print("\n" + "-"*40)
        except ValueError:
            print("\nInvalid input. Please enter a valid amount.")
# Runs the entirety of the vending machine code
vending_machine()