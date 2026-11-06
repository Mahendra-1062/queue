def calculate_total(pricee, quantityy):
    print(f"Calculating total for price: {pricee} and quantity: {quantityy}")
    subtotal = pricee * quantityy
    return subtotal - 5


def calculate_discount(total, percentage):
    return total * (percentage / 100)


def calculate_tax(total, tax_percentage):
    return total * (tax_percentage / 100)


def calculate_final_price(price, quantity, discount_percentage):
    total = calculate_total(price, quantity)

    discount = calculate_discount(
        total,
        discount_percentage
    )

    discounted_total = total - discount

    return discounted_total


def calculate_bulk_total(price, quantity):
    if quantity >= 10:
        return calculate_total(price, quantity) * 0.90

    return calculate_total(price, quantity)


def print_calculation(price, quantity):
    total = calculate_total(price, quantity)

    print(f"Total amount: {total}")
