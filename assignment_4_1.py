"""
Assignment 4 Problem 1: Currently, you have no way to count the number of times a substring matches within another string. To solve this problem, you will create two functions: countSubstrMatches and countSubstrRecursive. Both of these functions will take two arguments: a string to search and the substring you want to find. Your functions will both use the method find to identify the matches. The first function will search iteratively. The second function will search recursively. 
October 1, 2023
Aaman Bhandari
"""

from string import * #this line serves no purpose in the code 
"""
This function counts the number of times a specified substring appears within a given string. It does so iteratively, using Python's find method.

Arguments:

string (type: str): The main string within which we want to search for occurrences of the substring. This is the string we'll be examining.
substring (type: str): The substring we want to find and count within the main string.

Returns:

count (type: int): The number of times the specified substring appears within the main string.
"""
def countSubstrMatches(string, substring):
    """Counts the number of times a substring matches within another string iteratively."""
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

"""
This function counts the number of times a specified substring appears within a given string. Unlike the first function, it does this recursively.

Arguments:

string (type: str): The main string within which we want to search for occurrences of the substring.
substring (type: str): The substring we want to find and count within the main string.

Returns:

count (type: int): The number of times the specified substring appears within the main string.
"""

def countSubstrRecursive(string, substring):
    """Counts the number of times a substring matches within another string recursively."""
    pos = string.find(substring)
    if pos != -1:
        return 1 + countSubstrRecursive(string[pos+1:], substring)
    else:
        return 0

# Test the functions
testString = "atatattta"
test_string = "ababcabcabc"
test_substring = "abc"
test_string1 = testString.find("ata")
test_string2 = testString.find("ttt")
test_string3 = testString.find("ata",1)
test_string4 = "python".find("Python") 
iterative_count = countSubstrMatches(test_string, test_substring)
recursive_count = countSubstrRecursive(test_string, test_substring)

#Commented out for testing
# print(iterative_count, recursive_count) #prints 3 3
# print(test_string1, test_string2, test_string3, test_string4) #prints 0 5 2 -1
