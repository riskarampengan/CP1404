def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month ".format(month)))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()