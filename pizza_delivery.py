"""
Pizza Palace - Pizza Delivery App
Python Programming Project

I built this as a simple ordering system where a customer can
pick their pizza, add toppings, grab a drink, and check out.
Nothing fancy -- just parallel lists, some input validation,
and a printed receipt at the end.
"""

# --- menu data ---
# I kept everything in parallel lists to match what we learned in class.
# Each index lines up: name[0] goes with price[0], and so on.

SIZE_NAMES   = ["Small (10\")", "Medium (12\")", "Large (14\")", "XL (16\")"]
SIZE_PRICES  = [8.99,           11.99,            14.99,          17.99]

TOPPING_NAMES  = ["Pepperoni", "Mushrooms", "Onions", "Sausage",
                  "Bacon",     "Extra Cheese", "Bell Peppers", "Olives"]
TOPPING_PRICES = [1.50,        1.00,         0.75,    1.50,
                  1.50,        1.25,          0.75,    0.75]

CRUST_NAMES  = ["Thin Crust", "Regular Crust", "Thick Crust", "Stuffed Crust"]
CRUST_PRICES = [0.00,          0.00,             1.00,          2.50]

DRINK_NAMES  = ["Coke",  "Diet Coke", "Sprite", "Water", "Lemonade"]
DRINK_PRICES = [1.99,     1.99,        1.99,     0.99,    2.49]

TAX_RATE         = 0.08   # state tax is 8%
DELIVERY_FEE     = 3.99   # flat delivery charge
DISCOUNT_CODE    = "PIZZA10"
DISCOUNT_PERCENT = 0.10   # PIZZA10 knocks 10% off the order


# --- helper functions ---

def print_header(title):
    # just a quick way to make sections look cleaner in the terminal
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


def print_menu(names, prices, title):
    # loops through both lists at the same index and prints each option
    print_header(title)
    for i in range(len(names)):
        print(f"  {i + 1}. {names[i]:<20} ${prices[i]:.2f}")
    print("-" * 50)


def get_valid_int(prompt, low, high):
    # keeps asking until the user gives a real number that's in range
    # I used a try/except here to catch letters or symbols
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"  Pick a number from {low} to {high}.")
        except ValueError:
            print("  That didn't work -- please type a number.")


def get_yes_no(prompt):
    # simple yes/no loop, accepts y, yes, n, no (not case-sensitive)
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Just type Y or N.")


# --- order functions ---

def get_customer_info():
    # grab the basics -- name, address, phone
    print_header("Customer Information")
    name    = input("  Enter your name: ").strip()
    address = input("  Enter delivery address: ").strip()
    phone   = input("  Enter phone number: ").strip()
    return name, address, phone


def choose_size():
    # shows the size menu and returns what the customer picked
    print_menu(SIZE_NAMES, SIZE_PRICES, "Choose Your Size")
    choice = get_valid_int("  Enter size number: ", 1, len(SIZE_NAMES))
    return SIZE_NAMES[choice - 1], SIZE_PRICES[choice - 1]


def choose_crust():
    # same idea as choose_size, just for crust
    print_menu(CRUST_NAMES, CRUST_PRICES, "Choose Your Crust")
    choice = get_valid_int("  Enter crust number: ", 1, len(CRUST_NAMES))
    return CRUST_NAMES[choice - 1], CRUST_PRICES[choice - 1]


def choose_toppings():
    # customer can pick as many toppings as they want, one at a time
    # entering 0 means they're done
    print_menu(TOPPING_NAMES, TOPPING_PRICES, "Choose Your Toppings")
    selected = []
    print("  Enter topping numbers one at a time.")
    print("  Press 0 when done.\n")

    while True:
        choice = get_valid_int("  Add topping (0 to finish): ", 0, len(TOPPING_NAMES))
        if choice == 0:
            break
        name  = TOPPING_NAMES[choice - 1]
        price = TOPPING_PRICES[choice - 1]
        if (name, price) in selected:
            print(f"  Already got {name} on there.")
        else:
            selected.append((name, price))
            print(f"  Got it -- {name} added.")

    return selected


def build_pizza():
    # walks through size, crust, toppings and bundles it all into a dict
    size_name,  size_price  = choose_size()
    crust_name, crust_price = choose_crust()
    toppings                = choose_toppings()

    topping_total = sum(price for _, price in toppings)
    pizza_total   = size_price + crust_price + topping_total

    return {
        "size":          size_name,
        "size_price":    size_price,
        "crust":         crust_name,
        "crust_price":   crust_price,
        "toppings":      toppings,
        "topping_total": topping_total,
        "total":         pizza_total,
    }


def choose_drinks():
    # optional -- customer can skip drinks entirely or add multiple
    drinks = []
    if not get_yes_no("\n  Want to add drinks? (Y/N): "):
        return drinks

    print_menu(DRINK_NAMES, DRINK_PRICES, "Choose Drinks")
    print("  Enter drink numbers one at a time.")
    print("  Press 0 when done.\n")

    while True:
        choice = get_valid_int("  Add drink (0 to finish): ", 0, len(DRINK_NAMES))
        if choice == 0:
            break
        drinks.append((DRINK_NAMES[choice - 1], DRINK_PRICES[choice - 1]))
        print(f"  Added {DRINK_NAMES[choice - 1]}.")

    return drinks


def apply_discount(subtotal):
    # checks if the promo code matches -- if not, no discount
    code = input("\n  Got a promo code? (Enter to skip): ").strip().upper()
    if code == DISCOUNT_CODE:
        discount = round(subtotal * DISCOUNT_PERCENT, 2)
        print(f"  Nice! That saves you ${discount:.2f}")
        return discount
    elif code != "":
        print("  Hmm, that code didn't match anything.")
    return 0.00


# --- receipt ---

def print_receipt(customer, pizzas, drinks, discount, order_type):
    # prints out the full order breakdown at the end
    name, address, phone = customer
    print_header("Pizza Palace - Your Receipt")
    print(f"  Customer : {name}")
    print(f"  Phone    : {phone}")
    if order_type == "delivery":
        print(f"  Address  : {address}")
    print(f"  Order    : {'Delivery' if order_type == 'delivery' else 'Pickup'}")
    print("-" * 50)

    subtotal = 0.00

    # list each pizza with its parts
    for i, pizza in enumerate(pizzas, 1):
        print(f"\n  Pizza #{i}")
        print(f"    Size  : {pizza['size']:<25} ${pizza['size_price']:.2f}")
        print(f"    Crust : {pizza['crust']:<25} ${pizza['crust_price']:.2f}")
        if pizza["toppings"]:
            print("    Toppings:")
            for t_name, t_price in pizza["toppings"]:
                print(f"      - {t_name:<23} ${t_price:.2f}")
        print(f"    Pizza Subtotal:              ${pizza['total']:.2f}")
        subtotal += pizza["total"]

    # drinks section (only shows up if they ordered any)
    if drinks:
        print("\n  Drinks:")
        for d_name, d_price in drinks:
            print(f"    - {d_name:<25} ${d_price:.2f}")
            subtotal += d_price

    # delivery charge only applies if they chose delivery
    delivery_charge = DELIVERY_FEE if order_type == "delivery" else 0.00
    if order_type == "delivery":
        print(f"\n  Delivery Fee:                ${delivery_charge:.2f}")

    print("-" * 50)
    print(f"  Subtotal:                    ${subtotal:.2f}")

    if discount > 0:
        print(f"  Discount (10%):             -${discount:.2f}")
        subtotal -= discount

    tax   = round((subtotal + delivery_charge) * TAX_RATE, 2)
    total = round(subtotal + delivery_charge + tax, 2)

    print(f"  Tax (8%):                    ${tax:.2f}")
    print(f"  TOTAL:                       ${total:.2f}")
    print("=" * 50)
    print("  Thanks for ordering from Pizza Palace!")
    print("  Should be there in about 30-45 minutes.")
    print("=" * 50)


# --- main ---

def main():
    print_header("Welcome to Pizza Palace!")
    print("  Hot pizza, fast delivery -- let's get your order going.")

    # step 1: customer info
    customer = get_customer_info()

    # step 2: delivery or pickup?
    print_header("How do you want your order?")
    print("  1. Delivery")
    print("  2. Pickup")
    order_choice = get_valid_int("  Enter choice: ", 1, 2)
    order_type   = "delivery" if order_choice == 1 else "pickup"

    # step 3: build the pizzas
    pizzas = []
    while True:
        print_header(f"Building Pizza #{len(pizzas) + 1}")
        pizzas.append(build_pizza())
        print(f"\n  Pizza #{len(pizzas)} is in the order!")
        if not get_yes_no("  Want to add another pizza? (Y/N): "):
            break

    # step 4: drinks
    drinks = choose_drinks()

    # step 5: promo code
    pizza_subtotal = sum(p["total"] for p in pizzas)
    drink_subtotal = sum(price for _, price in drinks)
    discount = apply_discount(pizza_subtotal + drink_subtotal)

    # step 6: print the receipt
    print_receipt(customer, pizzas, drinks, discount, order_type)


if __name__ == "__main__":
    main()
