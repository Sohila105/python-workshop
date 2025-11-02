def add(cart):
    item = input("name: ")
    price = float(input("price: "))
    quantity = int(input("quantity: "))

    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": price, "quantity": quantity}
    print("item added")

def remove(cart):
    item = input("enter item name to remove: ")
    if item in cart:
        del cart[item]
        print(f"{item} removed")
    else:
        print("item not found")

def update(cart):
    item = input("item to update: ")
    if item in cart:
        quantity = int(input("new quantity: "))
        if quantity > 0:
            cart[item]["quantity"] = quantity
            print("quantity updated")
        else:
            del cart[item]
            print("quantity= 0")
    else:
        print("item not found")

def view(cart):
    subtotal = 0 
    discount = 0
    print("--- Cart Summary ---")
    print(f"{'Item':<10}{'Qty':<10}{'Price':<10}{'Total':<10}")
    print("--------------------------------------------------")
    for item, details in cart.items():
        total = details["price"] * details["quantity"]
        print(f"{item:<10}{details['quantity']:<10}${details['price']:<10}${total:<10}")
    subtotal += total
    if subtotal >100:
        discount= subtotal*0.1
    else:
        print("no discount")
    total= subtotal - discount
    print(f"Subtotal: ${subtotal}")
    print(f"Discount: ${discount}")
    print(f"Total: ${total}")
    

def checkout(cart):
    if not cart:
        print("your cart is empty")
    else:
        print("checking out..")
        view(cart)
        cart.clear()

def main():
    cart = {}
    while True:
        print("Shopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add(cart)
        elif choice == "2":
            remove(cart)
        elif choice == "3":
            update(cart)
        elif choice == "4":
            view(cart)
        elif choice == "5":
            checkout(cart)
        elif choice == "6":
            print("exit")
            break
        else:
            print("invalid")


if __name__ == "__main__":
    main()