"""
Assignment 4 Problem 4: The solution to problem three returns exact and fuzzy matches. The solution to this program is to create a function named fuzzyMatchesOnly that only returns string matches that are not an exact match. This function has two required arguments, the string that will be searched and a substring that you want to find. The output of this function is a tuple that provides the start position of fuzzy matches where one character is incorrect. (The returned tuple will not contain the start positions of exact matches.) 
October 1, 2023
Aaman Bhandari
"""
from assignment_4_3 import fuzzyMatching
from assignment_4_2 import allMatchesIndices

"""
The function identifies positions in a string where a sequence closely matches the provided substring, with exactly one character being different. It deliberately filters out exact matches to ensure only fuzzy matches are returned.

Arguments:

string (type: str): The main string within which we are searching for fuzzy matches.
substring (type: str): The substring against which we want to compare parts of the main string to identify fuzzy matches.

Returns:

fuzzy_only_matches (type: tuple of int): A tuple containing the starting indices in the main string where there are fuzzy matches (with exactly one character difference) to the provided substring.
"""

def fuzzyMatchesOnly(string, substring):
    """Returns start positions of only fuzzy matches and excludes exact matches."""
    # Get the start positions of exact matches for the substring
    exact_match_positions = allMatchesIndices(string, substring)
    
    # If the substring has only one character, there can't be a fuzzy match
    if len(substring) == 1:
        return ()
    
    # Split the substring into two parts for fuzzy matching
    mid = len(substring) // 2
    substring_1 = substring[:mid]
    substring_2 = substring[mid:]
    
    # Get potential fuzzy match positions using the logic from the previous function
    substring_1_positions = allMatchesIndices(string, substring_1)
    substring_2_positions = allMatchesIndices(string, substring_2)
    
    potential_fuzzy_matches = fuzzyMatching(substring_1_positions, substring_2_positions, len(substring_1))
    
    # Filter out the exact matches from the potential fuzzy matches
    fuzzy_only_matches = [pos for pos in potential_fuzzy_matches if pos not in exact_match_positions]
    
    return tuple(fuzzy_only_matches)

# Test the function
test_string = "abcdefgabad"
test_substring = "abcd"
fuzzy_only_results = fuzzyMatchesOnly(test_string, test_substring)

#Commented out for testing
# print(fuzzy_only_results) #()
