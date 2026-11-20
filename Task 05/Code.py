def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def calculate_bill(prices: list[float], gst_rate: float = 0.05) -> tuple[float, float]:
    subtotal = sum(prices)
    gst = subtotal * gst_rate
    return subtotal, gst


canteen_name = "Saveetha Canteen"


def scope_demo() -> str:
    counter = 0

    def increment_order():
        nonlocal counter
        local_note = "Order processed"
        counter += 1
        return f"{canteen_name} | {local_note} #{counter}"

    return increment_order()


def make_order_closure():
    items = []

    def add(item: str) -> list[str]:
        items.append(item)
        return list(items)

    return add


if __name__ == "__main__":
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print(add_item("Tea"), add_item("Vada"))
    print("add_item_buggy.__defaults__:", add_item_buggy.__defaults__)

    cust1 = add_item("Idli")
    add_item("Coffee", cust1)
    cust2 = add_item("Dosa")
    cust3 = add_item("Pongal")
    print("Customer 1:", cust1)
    print("Customer 2:", cust2)
    print("Customer 3:", cust3)

    total, gst = calculate_bill([30.0, 20.0], gst_rate=0.05)
    print(f"Subtotal: Rs.{total:.2f}, GST: Rs.{gst:.2f}, Grand Total: Rs.{total + gst:.2f}")

    print(scope_demo())
    c_closure = make_order_closure()
    print("Closure order:", c_closure("Samosa"), "->", c_closure("Chai"))
  
