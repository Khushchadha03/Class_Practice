from utils import ShoppingCart

catalog1 = {
    "apple": 1.00,
    "banana": 0.50,
    "milk": 2.50,
    "bread": 1.50,
    "chocolate": 3.00
}

cart = ShoppingCart(catalog1)
while True:
        command = input().strip()
        if command == "Exit":
            break

        parts = command.split()

        if parts[0] == "AddItem":
            item, qty = parts[1], int(parts[2])
            cart.add_item(item, qty)

        elif parts[0] == "RemoveItem":
            item, qty = parts[1], int(parts[2])
            cart.remove_items(item, qty)

        elif parts[0] == "CalculateTotal":
            cart.calculate_total_cost()

        elif parts[0] == "ApplyDiscounts":
            item, min_qty, discount_price = parts[1], int(parts[2]), float(parts[3])
            cart.apply_discounts(item, min_qty, discount_price)