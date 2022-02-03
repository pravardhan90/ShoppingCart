import sys
from Item import Item
from Cart import Cart

#initiazie the cart
cart = Cart()

#add item to cart on user input
def add_item():
    #get user inputs - name, qty and price of item
    name = input("Enter product name : ")
    qty = int(input("Enter product quantity : "))
    price = float(input("Enter product price: "))
    #add item to cart with user inputs
    cart.add_item(Item(name, price, qty))

#get product, tax and final totals of cart
def display_totals():
    print("No of items in cart : {}".format(cart.get_cart_qty()))
    print("Product cost        : {}".format(cart.get_product_total()))
    print("Tax                 : {}".format(cart.get_tax_total()))
    print("Total cost of cart  : {}".format(cart.get_cart_total()))

#loop terminates when user select 3(Exit)
#to add items to cart user to select 1
#to get total's anytime user to select 2
while True:
    try:
        choice = int(input("1.Add Item\n2.Totals\n3.Exist\nEnter your choice : "))
    except ValueError:
        print("\nERROR: Choose only digits from the given option")
        continue
    #choice for adding item
    if choice == 1:
        add_item()
    #to get total's of cart, that breaks loop
    elif choice == 2:
        display_totals()
        break   
    #Exit program at any point 
    else:
        sys.exit(0)

