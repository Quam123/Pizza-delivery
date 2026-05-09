"""
========================================================
  Pizza Palace - Pizza Delivery Application
  Course: Python Programming Project
  Description: A menu-driven pizza ordering system that
               allows customers to build orders, apply
               discounts, and receive an itemized receipt.
========================================================
"""

# ─────────────────────────────────────────────
#  MENU DATA  (Parallel lists)
# ─────────────────────────────────────────────

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

TAX_RATE         = 0.08   # 8% tax
DELIVERY_FEE     = 3.99
DISCOUNT_CODE    = "PIZZA10"
DISCOUNT_PERCENT = 0.10   # 10% off


# ─────────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────────

def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


def print_menu(names, prices, title):
    """Display a numbered menu with prices."""
    print_header(title)
    for i in range(len(names)):
        print(f"  {i + 1}. {names[i]:<20} ${prices[i]:.2f}")
    print("-" * 50)


def get_valid_int(prompt, low, high):
    """Prompt user until a valid integer in [low, high] is entered."""
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"  Please enter a number between {low} and {high}.")
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_yes_no(prompt):
    """Prompt user for a yes/no answer. Returns True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please enter Y or N.")


# ─────────────────────────────────────────────
#  ORDER FUNCTIONS
# ─────────────────────────────────────────────

def get_customer_info():
    """Collect customer name, address, and phone number."""
    print_header("Customer Information")
    name    = input("  Enter your name: ").strip()
    address = input("  Enter delivery address: ").strip()
    phone   = input("  Enter phone number: ").strip()
    return name, address, phone


def choose_size():
    """Let the customer choose a pizza size. Returns (name, price)."""
    print_menu(SIZE_NAMES, SIZE_PRICES, "Choose Your Size")
    choice = get_valid_int("  Enter size number: ", 1, len(SIZE_NAMES))
    return SIZE_NAMES[choice - 1], SIZE_PRICES[choice - 1]


def choose_crust():
    """Let the customer choose a crust type. Returns (name, price)."""
    print_menu(CRUST_NAMES, CRUST_PRICES, "Choose Your Crust")
    choice = get_valid_int("  Enter crust number: ", 1, len(CRUST_NAMES))
    return CRUST_NAMES[choice - 1], CRUST_PRICES[choice - 1]


def choose_toppings():
    """
    Let the customer choose multiple toppings.
    Returns a list of (name, price) tuples.
    """
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
            print(f"  {name} is already added.")
        else:
            selected.append((name, price))
            print(f"  ✓ {name} added.")

    return selected


def build_pizza():
    """
    Walk the customer through building one pizza.
    Returns a pizza dictionary.
    """
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
    """
    Let the customer add drinks to the order.
    Returns a list of (name, price) tuples.
    """
    drinks = []
    if not get_yes_no("\n  Would you like to add drinks? (Y/N): "):
        return drinks

    print_menu(DRINK_NAMES, DRINK_PRICES, "Choose Drinks")
    print("  Enter drink numbers one at a time.")
    print("  Press 0 when done.\n")

    while True:
        choice = get_valid_int("  Add drink (0 to finish): ", 0, len(DRINK_NAMES))
        if choice == 0:
            break
        drinks.append((DRINK_NAMES[choice - 1], DRINK_PRICES[choice - 1]))
        print(f"  ✓ {DRINK_NAMES[choice - 1]} added.")

    return drinks


def apply_discount(subtotal):
    """
    Ask the customer for a promo code.
    Returns the discount amount (0.00 if code is invalid).
    """
    code = input("\n  Enter promo code (or press Enter to skip): ").strip().upper()
    if code == DISCOUNT_CODE:
        discount = round(subtotal * DISCOUNT_PERCENT, 2)
        print(f"  ✓ Code accepted! You save ${discount:.2f}")
        return discount
    elif code != "":
        print("  Invalid promo code.")
    return 0.00


# ─────────────────────────────────────────────
#  RECEIPT
# ─────────────────────────────────────────────

def print_receipt(customer, pizzas, drinks, discount, order_type):
    """Print a fully itemized receipt."""
    name, address, phone = customer
    print_header("Pizza Palace - Order Receipt")
    print(f"  Customer : {name}")
    print(f"  Phone    : {phone}")
    if order_type == "delivery":
        print(f"  Address  : {address}")
    print(f"  Order    : {'Delivery' if order_type == 'delivery' else 'Pickup'}")
    print("-" * 50)

    subtotal = 0.00

    # Pizzas
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

    # Drinks
    if drinks:
        print("\n  Drinks:")
        for d_name, d_price in drinks:
            print(f"    - {d_name:<25} ${d_price:.2f}")
            subtotal += d_price

    # Delivery fee
    delivery_charge = DELIVERY_FEE if order_type == "delivery" else 0.00
    if order_type == "delivery":
        print(f"\n  Delivery Fee:                ${delivery_charge:.2f}")

    print("-" * 50)
    print(f"  Subtotal:                    ${subtotal:.2f}")

    # Discount
    if discount > 0:
        print(f"  Discount (10%):             -${discount:.2f}")
        subtotal -= discount

    tax   = round((subtotal + delivery_charge) * TAX_RATE, 2)
    total = round(subtotal + delivery_charge + tax, 2)

    print(f"  Tax (8%):                    ${tax:.2f}")
    print(f"  TOTAL:                       ${total:.2f}")
    print("=" * 50)
    print("  Thank you for ordering from Pizza Palace!")
    print("  Estimated delivery time: 30-45 minutes")
    print("=" * 50)


# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────

def main():
    """Main entry point — runs the full ordering workflow."""
    print_header("Welcome to Pizza Palace!")
    print("  Your neighborhood pizza delivery experts.")

    # Customer info
    customer = get_customer_info()

    # Delivery or pickup
    print_header("Order Type")
    print("  1. Delivery")
    print("  2. Pickup")
    order_choice = get_valid_int("  Enter choice: ", 1, 2)
    order_type   = "delivery" if order_choice == 1 else "pickup"

    # Build pizzas
    pizzas = []
    while True:
        print_header(f"Building Pizza #{len(pizzas) + 1}")
        pizzas.append(build_pizza())
        print(f"\n  ✓ Pizza #{len(pizzas)} added to your order!")
        if not get_yes_no("  Add another pizza? (Y/N): "):
            break

    # Drinks
    drinks = choose_drinks()

    # Discount
    pizza_subtotal = sum(p["total"] for p in pizzas)
    drink_subtotal = sum(price for _, price in drinks)
    discount = apply_discount(pizza_subtotal + drink_subtotal)

    # Receipt
    print_receipt(customer, pizzas, drinks, discount, order_type)


# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
