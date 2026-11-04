from user_service import get_user
from user_service import format_user
from user_service import validate_user

from calculator import calculate_total
from calculator import calculate_discount
from calculator import calculate_final_price


def create_order(user_id, price, quantity, discount_percentage):
    user = get_user(user_id)

    if not validate_user(user):
        return None

    final_price = calculate_final_price(
        price,
        quantity,
        discount_percentage
    )

    return {
        "user_id": user.user_id,
        "user_name": user.name,
        "total": final_price,
    }


def get_order_summary(user_id, price, quantity):
    user = get_user(user_id)

    if not user:
        return "User not found"

    total = calculate_total(price, quantity)

    return {
        "user": format_user(user),
        "total": total,
    }


def apply_order_discount(user_id, price, quantity, discount_percentage):
    user = get_user(user_id)

    if not user:
        return None

    total = calculate_total(price, quantity)

    discount = calculate_discount(
        total,
        discount_percentage
    )

    return {
        "user_id": user.user_id,
        "original_total": total,
        "discount": discount,
        "final_total": total - discount,
    }


def print_order(user_id, price, quantity, discount_percentage):
    order = create_order(
        user_id,
        price,
        quantity,
        discount_percentage
    )

    if order is None:
        print("Unable to create order")
        return

    print(order)


def get_customer_details(user_id):
    user = get_user(user_id)

    if not validate_user(user):
        return None

    return {
        "id": user.user_id,
        "name": user.name,
        "email": user.email,
    }
