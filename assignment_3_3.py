"""
Assignment 3 Problem 3: The cost per nugget by quantity varies. For this problem, you need to give the user the lowest cost option. Assume that the 6-piece option costs $3, the 9-piece costs $4, and the 22-piece costs $9. Instead of presenting all possible options, provide the least expensive option and the total cost, instead. When the user requests a quantity that is not feasible, let them know that their order quantity isn’t feasible and present the least expensive option and total cost for the suggested alternative quantity. You can think of this as a second Diophantine equation. While you still need to identify the values that satisfy the quantity requirements of 6a + 9b + 22c = n, there is an additional constraint 3a + 4b + 9c = cost (where 3, 4, and 9 represent the costs associated with the 6, 9, and 22-piece options, respectively).
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

def calculate_cost(a, b, c):
    """Calculate the total cost for the combination of boxes."""
    return 3*a + 4*b + 9*c

def order_nuggets_cheapest(n):
    """Prints the cheapest combination to order n chicken nuggets. If n is not feasible, provide the nearest feasible alternative with its cheapest combination."""
    combinations = find_combinations(n)
    if combinations:
        # Find the combination with the minimum cost
        min_cost = float('inf')
        best_combination = None
        for combo in combinations:
            cost = calculate_cost(*combo)
            if cost < min_cost:
                min_cost = cost
                best_combination = combo
        a, b, c = best_combination
        print(f"The cheapest way to order {n} chicken nuggets is:")
        print(f"'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
        print(f"Total cost: ${min_cost}")
    else:
        # Find the nearest feasible quantity and its cheapest combination
        nearest_feasible = find_nearest_feasible(n)
        combinations_alternative = find_combinations(nearest_feasible)
        min_cost = float('inf')
        best_combination = None
        for combo in combinations_alternative:
            cost = calculate_cost(*combo)
            if cost < min_cost:
                min_cost = cost
                best_combination = combo
        a, b, c = best_combination
        print(f"Sorry, you cannot order {n} chicken nuggets with the given box sizes.")
        print(f"However, the cheapest way to order {nearest_feasible} chicken nuggets is:")
        print(f"'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
        print(f"Total cost: ${min_cost}")

# Sample use
n = int(input("How many chicken nuggets would you like to order? "))
order_nuggets_cheapest(n)
