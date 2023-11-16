"""
Assignment 3 Problem 1:  Assume that you can purchase chicken nuggets in quantities of 6, 9, and 22. That means that there is no combination of options that will allow you to purchase 23 chicken nuggets. In terms of the Diophantine equation, you can think of it as 6a + 9b + 22c = n. To achieve this objective, there are four specific requirements. Start by asking the user how many chicken nuggets they would like to order. For each possible order quantity by box size identify which combinations equivalent to n(in other words, look for what values of a, b, and c in the Diophantine equation work). If the order is possible, print a statement to the console that states how many options are available and what these options are (a console output example is shown in Figure 2). If there are no combinations that work (such as an order of 23), let them know that they cannot order the requested quantity.
September 24, 2023
Aaman Bhandari
"""

def find_combinations(n):
    """
    Returns all possible combinations of a, b, and c such that 6a + 9b + 22c = n.
    """
    # List to store the possible combinations
    combinations = []

    # Loop through all possible values of a, b, and c
    for a in range(0, n//6 + 1):
        for b in range(0, n//9 + 1):
            for c in range(0, n//22 + 1):
                if 6*a + 9*b + 22*c == n:
                    combinations.append((a, b, c))
    
    return combinations
def order_nuggets(n):
    """
    Prints the possible combinations to order n chicken nuggets.
    """
    # Get the possible combinations
    combinations = find_combinations(n)

    # If there are possible combinations, print them
    if combinations:
        print(f"For an order size of {n}, choose from the following {len(combinations)} options:")
        for a, b, c in combinations:
            
            print(f"'Six_piece': {a}, 'Nine_piece': {b}, 'Twenty_two_piece': {c}")
            
    else:
        # If not, let the user know
        print(f"Sorry, you cannot order {n} chicken nuggets with the given box sizes.")

# Prompt the user for the number of chicken nuggets
n = int(input("How many chicken nuggets would you like to order? "))
order_nuggets(n)