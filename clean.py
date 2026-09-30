def multiply_values(first_factor, second_factor):
    """Return the product of two values."""
    return first_factor * second_factor
def add_adjustment(value, adjustment):
    """Add an adjustment to a value."""
    return value + adjustment
def divide_by_two(value):
    """Return half of a value."""
    return value / 2
def calculate_result(first_factor, second_factor, adjustment):
    """Multiply two values, add an adjustment, and return half the total."""
    # Preserve the original operation order.
    product = multiply_values(first_factor, second_factor)
    adjusted_total = add_adjustment(product, adjustment)
    return divide_by_two(adjusted_total)
print(calculate_result(4, 6, 1))