# Electricity with Tarrif 11 or 31

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
daily_use = float(input("Enter daily use in kWh: "))
billing_number_days = int(input("Enter number of billing days: "))
tariff_input = int(input("Choose between Tariff 11 or 31: "))
if tariff_input == 11:
    calculate = (daily_use * billing_number_days * TARIFF_11)/100
    print(round(calculate, 2))
elif tariff_input == 31:
    calculate = (daily_use * billing_number_days * TARIFF_31)/100
    print(round(calculate, 2))
else:
    print("Invalid input")