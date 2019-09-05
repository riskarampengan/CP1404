my_dictionary = {}
user_input = input("Text: ")
words = user_input.split()

for word in words:
    if word in my_dictionary:
        my_dictionary[word] += 1
    else:
        my_dictionary[word] = 1

for key, value in my_dictionary.items():
        print('{}: {}'.format(key, value))