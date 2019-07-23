name = str(input("Enter name: "))
user_choice = ""

valid_inputs = ["H", "G", "Q"]
while user_choice != "Q":
    print("(H)ello\n"
          "(G)oodbye\n"
          "(Q)uit")
    user_choice = str(input("Enter choice: "))
    user_choice = user_choice.upper()
    if user_choice == "H":
        print("Hello " + name)
    elif user_choice == "G":
        print("Goodbye " + name)
    elif user_choice == "Q":
        print("Finished")
    else:
        print("Invalid choice")