"""
Assignment 5 Problem 1: Create a function named fixedInvestor. This function has four required arguments: the employee salary, the employee's personnel investment rate as a percentage of their salary, a fixed growth rate of the retirement plan, and the number of years to evaluate the growth. This function will return a list with the total value of the retirement plan at the end of each year. For the solution, the retirement account is compounded annually. The fixed growth rate of the retirement plan is not used when calculating the first year's return. The formula is the salary multiplied by the rate the employee invested, the rate employer invested, and the rate that the employer matched. In the second year, interest is earned by calculating the earnings from the first year multiplied by the investment growth rate.
October 8, 2023
Aaman Bhandari
"""

"""
    Calculate the total value of a retirement plan at the end of each year.
    
    Parameters:
    - salary (float): Employee's annual salary.
    - investment_rate (float): Employee's personal investment rate as a fraction (e.g., 0.15 for 15%).
    - growth_rate (float): Annual growth rate of the retirement plan as a fraction (e.g., 0.05 for 5%).
    - years (int): Number of years to evaluate the growth.
    
    Returns:
    - list: List of total values of the retirement plan at the end of each year.
    
    Example:
    If an employee has a salary of $50,000, invests 15% of it, and the growth rate is 5% for 3 years,
    the output will be [7500.0, 15375.0, 23643.75].
"""

def fixedInvestor(salary, investment_rate, growth_rate, years):
    total_values = []
    previous_year_value = 0
    
    for year in range(1, years + 1):
        contribution = salary * investment_rate
        total_value = contribution + previous_year_value * (1 + growth_rate)
        total_values.append(total_value)
        previous_year_value = total_value
    
    return total_values

# Testing the function with the given example:
test_salary = 50000
test_investment_rate = 0.15
test_growth_rate = 0.05
test_years = 3

test_results = fixedInvestor(test_salary, test_investment_rate, test_growth_rate, test_years)
#print(test_results)