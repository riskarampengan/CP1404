# If the total price is more than $100, the person gets 10% discount

items = int(input("Enter number of items: "))
item_list = [float(input("Enter item's price: ")) for i in range(items)]
total_item = sum(item_list)
if total_item > 100:
    total_price = total_item - (total_item * 10/100)
    print("$", total_price)
else:
    print("$", total_item)