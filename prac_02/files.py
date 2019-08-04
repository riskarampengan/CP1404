# Task 1

name = str(input("Enter name: "))
file = open('name.txt', 'w')
file.write(name)
file.close()

# Task 2
file = open('name.txt', 'r')
name = file.read().strip()
file.close()
print("Your name is ", name)

# Task 3
file = open('numbers.txt', 'r')
number_1 = int(file.readline())
number_2 = int(file.readline())
file.close()
print(number_1 + number_2)

# Task 4
file = open('numbers.txt', 'r')
total = 0
for line in file:
    number = int(line)
    total += number
file.close()
print(total)