inventory = {}

while True:
    print("1.Add 2.View 3.Exit")
    choice = input("Choice: ")
    if choice == '1':
        item = input("Item: ")
        qty = int(input("Qty: "))
        inventory[item] = qty
    elif choice == '2':
        print(inventory)
    elif choice == '3':
        break
