"""
Assignment 5 Problem 4: How much can be spent from a retirement account every year to use all of the money? To answer this question, create a function named maximumExpensed. This function has five required arguments: salary, the percentage rate saved, a list of annual return rates while investing, a list of annual return rates while retired and a value for epsilon. The number of values in the list of annual return rates while investing represents the number of years worked. The number of values in the list of return rates while retired represents the years between retirement and bankruptcy (or when one might expect to pass on). Use the idea of binary searching to find a value for the amount expensed when retired so that the value of the retirement account is very close to zero. Keep in mind that it may be a negative number. (The values represent approximations of unrealized gains and losses, so overdrawing the account by a small amount is acceptable). Use the solution from problem two to determine the value saved. Likewise, use your solution to problem three to determine how much money remains at the end. While your function is searching for the solution, print the expensed and remaining value in a complete sentence to the console each time the expensed value changes.
October 8, 2023
Aaman Bhandari
"""
from assignment_5_3 import finallyRetired
from assignment_5_2 import variableInvestor

def maximumExpensed(salary, savings_rate, investing_rates, retirement_rates, epsilon):
    """
    Determine the maximum amount that can be expensed from a retirement account every year such that the account is nearly depleted at the end of retirement.
    
    Parameters:
    - salary (float): Employee's annual salary.
    - savings_rate (float): Percentage rate saved as a fraction (e.g., 0.15 for 15%).
    - investing_rates (list): List of annual return rates while investing.
    - retirement_rates (list): List of annual return rates while retired.
    - epsilon (float): Tolerance level for how close the final balance should be to zero.
    
    Returns:
    - float: Maximum annual expense amount.
    """
    
    # Calculate initial retirement savings using the variableInvestor function
    retirement_principal = variableInvestor(salary, savings_rate, investing_rates)[-1]
    
    # Binary search to find the maximum annual expense
    low = 0
    high = retirement_principal / len(retirement_rates)  # A rough upper bound
    best_expense = 0
    
    while high - low > epsilon:
        mid = (high + low) / 2
        remaining_balance = finallyRetired(retirement_principal, retirement_rates, mid)[-1]
        
        if remaining_balance > epsilon:
            # If there's still money left, we can try increasing the annual expense
            low = mid
        else:
            # If we've overspent, decrease the annual expense
            high = mid
        best_expense = mid
        print(f"With an annual expensed amount of ${best_expense:.2f}, the remaining balance at the end is ${remaining_balance:.2f}.")
    
    return best_expense

# Testing the function with an example:
test_salary = 50000
test_savings_rate = 0.15
test_investing_rates = [0, 0.05, 0.06]
test_retirement_rates = [0.05, 0.04, 0.03, 0.02, 0.01]  # 5 years of retirement for this test
test_epsilon = 0.01

maximum_expensed_amount = maximumExpensed(test_salary, test_savings_rate, test_investing_rates, test_retirement_rates, test_epsilon)
#print(maximum_expensed_amount)
