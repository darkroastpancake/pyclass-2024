# Stock
muffins = 10
cupcakes = 10

# Selling
while True:
    item = input("Enter 'muffin' or 'cupcake' for purchase, or '0' to finish: ").strip().lower()
    
    if item == '0':
        # When done selling, print the remaining stock and exit
        print(f"muffins: {muffins} cupcakes: {cupcakes}")
        break
    elif item == 'muffin':
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif item == 'cupcake':
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    else:
        print("Invalid input. Please enter 'muffin', 'cupcake', or '0'.")
