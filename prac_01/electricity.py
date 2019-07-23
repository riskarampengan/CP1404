price = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_number_days = int(input("Enter number of billing days: "))
bill = ((price * daily_use) / 100) * billing_number_days

print("$ ", bill)