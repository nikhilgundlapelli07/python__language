
# Personal Expense Calculator

def calculate_total(food, travel, shopping, other):
    total = food + travel + shopping + other
    return total


def check_expense(total):
    if total > 5000:
        print("You spent too much money!")
    else:
        print("Your expenses are under control.")


def main():
    print("===== Personal Expense Calculator =====")

    food = float(input("Enter food expenses: "))
    travel = float(input("Enter travel expenses: "))
    shopping = float(input("Enter shopping expenses: "))
    other = float(input("Enter other expenses: "))

    total = calculate_total(food, travel, shopping, other)

    print("\n----- Expense Report -----")
    print("Food:", food)
    print("Travel:", travel)
    print("Shopping:", shopping)
    print("Other:", other)
    print("Total Expenses:", total)

    check_expense(total)


main()
