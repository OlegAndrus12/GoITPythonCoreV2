# bad code
try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
except ValueError:
    print("Invalid input ")

print("Total price:", total)  # crash if input failed


# better code
try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
except ValueError:
    print("Invalid input ")
else:
    print("Total price:", total)