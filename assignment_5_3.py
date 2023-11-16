"""
Assignment 5 Problem 3: Once retired, it would be important to know how much an account is changing because the account is still earning interest, but fixed payments are distributed from the retirement account to the retiree. To solve this problem, create a function named finallyRetired. This function has three arguments. The first is the amount of money in the retirement account. The second value is a list of the annual rates of return, and the third is the annual amount expensed to the retiree. When retiring, there is already an established principal, so there is interest earned every year in this solution.
October 8, 2023
Aaman Bhandari
"""

def finallyRetired(principal, annual_rates, annual_expense):
    """
    Calculate the retirement account balance over the years, taking into account interest earned and fixed payments to the retiree.
    
    Parameters:
    - principal (float): Initial amount in the retirement account.
    - annual_rates (list): List of annual rates of return as fractions (e.g., [0.05, 0.06] for 5% and 6% respectively).
    - annual_expense (float): Annual amount expensed to the retiree.
    
    Returns:
    - list: List of retirement account balances at the end of each year.
    """
    
    balances = []
    
    for rate in annual_rates:
        interest_earned = principal * rate
        principal = principal + interest_earned - annual_expense
        balances.append(principal)
    
    return balances

# Testing the function with an example:
test_principal = 23797.5  # The balance at the end of the third year from the previous example
test_annual_rates = [0.05, 0.04, 0.03]
test_annual_expense = 5000

finallyRetired_results = finallyRetired(test_principal, test_annual_rates, test_annual_expense)
#print(finallyRetired_results)
