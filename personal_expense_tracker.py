
# Personal Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Shopping/Other): ")

    if amount <= 0:
        print("Please enter a valid amount!")
        return

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet!")
        return

    print("\n----- EXPENSE HISTORY -----")

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - Rs.{expense['amount']:.2f} - {expense['category']}")


def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print("Total Expenses: Rs.", total)


def search_expense():
    search = input("Enter expense name to search: ").lower()

    found = False

    for expense in expenses:
        if search in expense["name"].lower():
            print(expense)
            found = True

    if not found:
        print("Expense not found!")


while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Search Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
