"""
Assignment 3 Problem 2: For this problem, it has been determined that it is simply not enough to tell the user their requested size is not feasible. You need to determine the closest feasible value of n given the quantity ordered by the user. Let the user know that their requested quantity is not feasible, but let them know they have options, by providing the quantity by box size options for this alternative feasible quantity.
September 24, 2023
Aaman Bhandari
"""

def find_combinations(n):
    """Returns all possible combinations of a, b, and c such that 6a + 9b + 22c = n."""
    combinations = []
    for a in range(0, n//6 + 1):
        for b in range(0, n//9 + 1):
            for c in range(0, n//22 + 1):
                if 6*a + 9*b + 22*c == n:
                    combinations.append((a, b, c))
    return combinations

def find_nearest_feasible(n):
    """Find the nearest feasible quantities (both less than and greater than n) until a feasible quantity is found."""
    lower_feasible = n - 1
    higher_feasible = n + 1
    while lower_feasible > 0:
        if find_combinations(lower_feasible):
            return lower_feasible
        lower_feasible -= 1
    while True:
        if find_combinations(higher_feasible):
            return higher_feasible
        higher_feasible += 1

def order_nuggets_with_alternative(n):
    """Prints the possible combinations to order n chicken nuggets. If n is not feasible, provide the nearest feasible alternative."""
    combinations = find_combinations(n)
    if combinations:
        print(f"For an order size of {n}, choose from the following {len(combinations)} options:")
        for a, b, c in combinations:
            print(f"'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
    else:
        nearest_feasible = find_nearest_feasible(n)
        combinations_alternative = find_combinations(nearest_feasible)
        print(f"Sorry, you cannot order {n} chicken nuggets with the given box sizes.")
        print(f"However, you can order {nearest_feasible} chicken nuggets in the following ways:")
        for a, b, c in combinations_alternative:
            print(f"'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")

# Sample use
n = int(input("How many chicken nuggets would you like to order? "))
order_nuggets_with_alternative(n)
