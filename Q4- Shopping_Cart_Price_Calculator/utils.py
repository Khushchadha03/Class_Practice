from typing import List, Optional, Dict

class ShoppingCart:
    def __init__(self, catalog:Dict[str, float])->None:
        self.catalog = catalog
        self.cart:Dict[str, int] = {}
        self.discounts: list[Dict[str,float | int | str]] = []

    def add_item(self, item: str, quantity: int)->None:
        if item not in self.catalog:
            print(f"{item} is not available oin the catalog")
            return
        self.cart[item] = self.cart.get(item,0) +quantity
        print(f"Added {quantity} {item}(s) in the cart.")

    def remove_items(self, item: str, quantity: int)->None:
        if item not in self.cart:
            print(f"{item} not available in the cart.")
            return
        self.cart[item]-=quantity
        if self.cart[item] <=0:
            del self.cart[item]
            print(f"Removed {quantity} {item}(s) for the cart.")

    def calculate_total_cost(self)->float:
        total = self.recursive_calculate_total_cost(list(self.cart.items()), 0)
        total = round(total, 2)
        print(f"Total Cost: ${total:.2f}")
        return total
    
    def recursive_calculate_total_cost(self, items: List, index: int)-> float:
        if index == len(items):
            return 0
        item, qty = items[index]
        return self.catalog[item] * qty + self.recursive_calculate_total_cost(items, index+1)
    
    def apply_discounts(self, item:str, min_qty: int, discount_price: float)-> float:
        rule = {"item": item, "min_qty": min_qty, "discount_price": discount_price}
        self.discounts.append(rule)

        discounted_total = self.apply_discounts_recursive(list(self.cart.items()),0,0)
        discounted_total = round(discounted_total, 2)

        original_total = self.calculate_total_cost()
        if discount_price < original_total:
            print(f"Discount Applied: ${discounted_total:.2f}.")
        else:
            print("No eligible discounts found.")

        return discounted_total
    
    def apply_discounts_recursive(self, items: List, index: int, total: float)-> float:
        if index == len(items):
            return total
        item, qty = items[index]
        discounted_price = self.catalog[item]
        for r in self.discounts:
            if r["item"] ==item and qty>= r["min_qty"]:
                discounted_price = r["discount_price"]
            total+= discounted_price * qty
            return self.apply_discounts_recursive(items, index + 1, total)