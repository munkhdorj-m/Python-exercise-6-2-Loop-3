def product_of_digits(num):
    num = abs(num)
    product = 1

    # Special case: if num is 0 → product is 0
    if num == 0:
        return 0

    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10

    return product


def sum_even_or_odd(num):
    num = abs(num)
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    if total % 2 == 0:
        return "Even"
    else:
        return "Odd"


def contains_five(num):
    num = abs(num)

    # Special case: num = 0
    if num == 0:
        return False

    while num > 0:
        digit = num % 10
        if digit == 5:
            return True
        num //= 10

    return False


def sum_even_digits(num):
    num = abs(num)
    total = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            total += digit
        num //= 10

    return total
