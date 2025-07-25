import pandas as pd
import os

# Define the CSV file where expenses will be stored
CSV_FILE = "expenses.csv"

# Function to load expenses from the CSV file
def load_expenses():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount"])

# Function to save expenses to the CSV file
def save_expenses(expenses):
    expenses.to_csv(CSV_FILE, index=False)

# Function to add a new expense
def add_expense(date, category, amount):
    expenses = load_expenses()
    new_expense = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    save_expenses(expenses)
    print("Expense added successfully!")

# Function to view total spending per category
def view_total_spending():
    expenses = load_expenses()
    total_per_category = expenses.groupby("Category")["Amount"].sum().reset_index()
    print("\nTotal Spending per Category:")
    print(total_per_category)

# Function to display the menu and get user input
def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Total Spending per Category")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the expense category: ")
            amount = float(input("Enter the amount: "))
            add_expense(date, category, amount)
        elif choice == "2":
            view_total_spending()
        elif choice == "3":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
