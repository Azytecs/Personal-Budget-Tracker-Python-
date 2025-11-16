#Task2
"""
Brief summary.

Parameters:
    param_name (type): Description.

Returns:
    return_type: Description.
"""

transactions=[]
def display_menu():
   """
    Displays the main menu and routes user input to the appropriate function.

    Parameters:
        None

    Returns:
        None: Continuously prompts the user until they choose to exit.
    """
   while True:
    print("")
    print("        ---Personal Budget Tracker--")
    #Added all options in one print line
    print("1. Add Income\n2. Add Expense\n3. List Transactions\n4. Delete Transaction\n5. View Overall Summary\n6. View Summary by Category\n7. Exit")
    try:
        answer= int(input("Please enter your choice: "))
    except ValueError:
        print("Enter a number from the given options")
        display_menu()
    print()
    if answer==1:
        add_transaction(transactions,"Income")
    elif answer==2:
        add_transaction(transactions,"Expense")
    elif answer==3:
         list_transactions(transactions)
    elif answer==4:
        delete_transaction(transactions)
    elif answer==5:
        print_overall_summary(calculate_summary(transactions))
    elif answer==6:
        print_summary_by_category(transactions)
    elif answer==7:
        break
#Task 3
def add_transaction(current_transactions, transaction_type):
    """
    Adds a new transaction to the list with user-provided details.

    Parameters:
        current_transactions (list): The list storing all transaction dictionaries.
        transaction_type (str): Either 'Income' or 'Expense', indicating the transaction type.

    Returns:
        None: Appends the new transaction to the list.
    """
    while True:
        try:
            amount = float(input(f"Enter {transaction_type} amount: "))
            if amount < 0:
                print("Invalid amount. Must be positive.")
            else:
                break  
        except ValueError:
            print("Amount must be a number.")

    description=input("Enter a description: ")
    category=input("Enter a Category: ")

    transaction_dictionary={"type":transaction_type,
                            "amount":amount,
                            "description":description,
                            "category":category}   
    print(f"{transaction_type} of £{amount} added successfully.")
    current_transactions.append(transaction_dictionary)
#Task 4
    
def list_transactions(transactions):
    """
    Displays all transactions with their details in a numbered list.

    Parameters:
        transactions (list): A list of transaction dictionaries.

    Returns:
        None: Prints each transaction with its index and details.
    """

    if len(transactions)==0:
        print("No transaction found")
    else:
        print("")
        print("   ---All Transactions--")
        for index, items in enumerate(transactions,start=1):
            print(f"{index}. [{items['type']}] - £{items['amount']} - {items['description']} (Category: {items['category']})")
#Task 5

def delete_transaction(transactions):
    """
    Deletes a transaction from the list based on user-selected index.

    Parameters:
        transactions (list): A list of transaction dictionaries.

    Returns:
        None: Removes the selected transaction from the list.
    """
    print("   ---Delete Transactions---   ")
    state=True
    if len(transactions)==0:
        print("List is empty")
        return
    else:
        for index, items in enumerate(transactions,start=1):
            print(f"{index} {items['type']} - £{items['amount']} - Description: {items['description']} - Category: {items['category']} ")
        while state==True:
            try:
                num_of_trans= (int(input("Enter number of the transaction to delete: ")))
                if(num_of_trans>0 and num_of_trans<=len(transactions)):
                    transactions.pop(num_of_trans-1)
                    print(f"Transaction deleted successfully.")
                    state=False
                else:
                   print("Input must match a transaction index")
            except ValueError:
                print("Input must match a transaction index")
#Task 6
def calculate_summary(transactions):
    """
    Calculates total income, total expenses, and net balance from the transaction list.

    Parameters:
        transactions (list): A list of transaction dictionaries.

    Returns:
        dict: A dictionary containing 'Total Income', 'Total Expense', and 'Net balance'.
    """
    total_expense=0
    total_income=0
    for items in transactions:
        if items['type']=="Expense":
            total_expense+=items['amount']
        elif items['type']=="Income":
            total_income+=items['amount']
    sumarry_data={"Total Income": total_income,
           "Total Expense": total_expense,
           "Net balance": total_income-total_expense}
    return sumarry_data

def print_overall_summary(summary_data):
    """
    Prints the overall financial summary including income, expenses, and net balance.

    Parameters:
        summary_data (dict): A dictionary with keys 'Total Income', 'Total Expense', and 'Net balance'.

    Returns:
        None: Outputs the summary to the console.
    """
    print()
    print("--- Summary Data ---")
    print(f"Total Income - {summary_data['Total Income']}")
    print(f"Total Expense - {summary_data['Total Expense']}")
    print(f"Net Balance - {summary_data['Net balance']}")

def print_summary_by_category(transactions):
    """
    Prints total expenses grouped by category.

    Parameters:
        transactions (list): A list of transaction dictionaries.

    Returns:
        None: Outputs category-wise expense summary to the console.
    """
    category_amount = {}
    print("--- Expenses by Category ---")

    if len(transactions) == 0:
        print("Empty Transaction List")
        return

    for items in transactions:
        if items['type'] == "Expense":  
            category = items['category']
            amounts = items['amount']
            if category not in category_amount:
                category_amount[category] = 0
            category_amount[category] += amounts

    for keys, values in category_amount.items():
        print(f"{keys}: £{values:.2f}")

    print("----------------------------")
display_menu()