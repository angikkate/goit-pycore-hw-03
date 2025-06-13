import random

def get_numbers_ticket(min_value, max_value, quantity):
    # validate the input parameters
    if min_value < 1 or max_value > 1000 or min_value > max_value:
        return []

    # create a list of possible numbers
    numbers = list(range(min_value, max_value + 1))

    # if quantity is more than available numbers — return an empty list
    if quantity > len(numbers):
        return []

    # select random unique numbers
    result = random.sample(numbers, quantity)

    # return the sorted list
    return sorted(result)

# Example of using:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)