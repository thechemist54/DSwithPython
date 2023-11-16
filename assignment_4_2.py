"""
Assignment 4 Problem 2: The second problem is that you do not have a function that will collect the start positions of every match between a substring and a string. For this solution, you will create one function named allMatchesIndices. This function will require two arguments, the string you need to search and the substring you want to find. The function shall return a tuple of the start indices of all matches.  
October 1, 2023
Aaman Bhandari
"""
"""
The function searches for all occurrences of a specified substring within a given string and returns the starting indices of each of these occurrences.

Arguments:

string (type: str): The main string within which we want to search for occurrences of the substring.
substring (type: str): The substring we want to find within the main string.

Returns:

indices (type: tuple of int): A tuple containing the starting indices of all matches of the specified substring within the main string.
"""
def allMatchesIndices(string, substring):
    """Returns a tuple of the start indices of all matches of the substring within the string."""
    indices = []
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            indices.append(pos)
            start = pos + 1
        else:
            break
    return tuple(indices)

# Test the function
test_string = "abatatatataca"
test_substring = "ata"
match_indices = allMatchesIndices(test_string, test_substring)

#Commented out for testing
# print(match_indices) #(2, 4, 6, 8)
# print(allMatchesIndices("atatattta", "ata")) #this doesn't give (1,) the ata starts at 0 and 2 which means it gives (0,2)
# print(allMatchesIndices("atatatatta", "ata")) #(0, 2, 4)
# print(allMatchesIndices("atattatta", "Python")) #()
