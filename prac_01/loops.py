# Odds number between 1 and 20 with a space between each one
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# Count down from 20 o 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Print n stars based from user input
#user_input = int(input("Enter number of stars: "))
#star_list= ["*" for i in range(user_input)]
#print (' '.join(["%s" % i for i in star_list]))

user_input = int(input("Enter number of stars: "))
for i in range(0, user_input):
    print("*", end=" ")
print()

# Print n lines of increasing stars

user_input = int(input("Enter number of stars: "))
for i in range(0, user_input):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

# Add loops on the sales bonus exercise until user enter negative number

sales = 1
while sales > 0:
    sales = float(input("Enter sales: $"))
    if sales > 0 and sales < 1000:
        calculate = (10/100)* sales
        print(calculate)
    elif sales >= 1000:
        calculate = (15/100)* sales
        print(calculate)
    else:
        print("Invalid!")
        exit()