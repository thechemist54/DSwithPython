"""
Assignment 5 Problem 2: It's been identified that the growth rate of an investment may not be static—that it may change over time. For this solution, create a function named variableInvestor. This function will have three arguments, similar to problem one. There is one distinct change. The growth rates of the investment plan will be fed to this function as a list. There will be a rate for each year of investing (i.e., if five years of calculations are needed, then the list of growth rates will contain five values). If you consider the list, the rate for the first year can be any value because interest is not earned. The function will no longer use the argument that represents the number of years needed. (The list length will be sufficient to determine the number of years.)
October 8, 2023
Aaman Bhandari
"""

def variableInvestor(salary, investment_rate, growth_rates):
    """
    Calculate the total value of a retirement plan at the end of each year with variable growth rates.
    
    Parameters:
    - salary (float): Employee's annual salary.
    - investment_rate (float): Employee's personal investment rate as a fraction (e.g., 0.15 for 15%).
    - growth_rates (list): List of annual growth rates of the retirement plan as fractions (e.g., [0, 0.05, 0.06] for 0%, 5%, and 6% respectively).
    
    Returns:
    - list: List of total values of the retirement plan at the end of each year.
    """
    
    total_values = []
    previous_year_value = 0
    
    for growth_rate in growth_rates:
        contribution = salary * investment_rate
        total_value = contribution + previous_year_value * (1 + growth_rate)
        total_values.append(total_value)
        previous_year_value = total_value
    
    return total_values

# Testing the function with an example:
test_growth_rates = [0, 0.05, 0.06]
test_salary = 50000
test_investment_rate = 0.15
variableInvestor_results = variableInvestor(test_salary, test_investment_rate, test_growth_rates)
#print(variableInvestor_results)
