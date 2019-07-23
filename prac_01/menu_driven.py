user_input = [int(input("Enter the number: ")) for i in range(2)]


for number in range(user_input[0], user_input[1]+1):
    if number % 2 == 0:
        print("Even number: ", number)
for number in range(user_input[0], user_input[1]+1):
    if number % 2 == 1:
        print("Odd number: ", number)
for number in range(user_input[0], user_input[1]+1):
    print("The square number: ", number ** 2)