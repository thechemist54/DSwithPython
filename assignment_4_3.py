"""
Assignment 4 Problem 3: Your goal is to find where all but one character in a substring match by creating a function named fuzzyMatching. For example, suppose the substring is abcd. In that case, positive matches include abc*, ab*d, a*cd, and *bcd (where * represents a wild card that any character can substitute). The function fuzzyMatching has three required arguments. The first argument is a tuple of matching start positions for the first substring (the tuple output of the function you created to solve the second problem). The second required argument is a tuple of the second substring. The length of the first substring is the third argument. The function returns a tuple of start positions of all fuzzy matches.  
October 1, 2023
Aaman Bhandari
"""

from assignment_4_2 import allMatchesIndices


"""
The function identifies starting positions in a string where a sequence (formed by combining two substrings with a wildcard in between) matches. The primary use case is for fuzzy matching where all but one character in a substring match within a given string.

Arguments:

start_positions_1 (type: tuple of int): The tuple containing starting positions of matches for the first substring within the main string.

start_positions_2 (type: tuple of int): The tuple containing starting positions of matches for the second substring within the main string.

length_1 (type: int): The length of the first substring.

num_wildcards (type: int, default value: 1): The number of wildcard characters that can substitute any other character. By default, it is set to 1.

Returns:

matched_positions (type: tuple of int): A tuple containing the starting indices in the main string where the sequence (formed by combining the two substrings with the wildcard(s) in between) matches.
"""

def fuzzyMatching(start_positions_1, start_positions_2, length_1, num_wildcards=1):
    """Returns start positions of fuzzy matches based on the specified logic."""
    matched_positions = []
    
    # Calculate the total adjustment based on the length of the first substring and number of wildcards
    adjustment = length_1 + num_wildcards
    
    # Check each start position from the first tuple
    for pos in start_positions_1:
        if pos + adjustment in start_positions_2:
            matched_positions.append(pos)
    
    return tuple(matched_positions)

# Test the function based on the provided example
substring_1_positions = allMatchesIndices("abcdefgabad", "a")
substring_2_positions = allMatchesIndices("abcdefgabad", "cd")
length_substring_1 = len("a")

fuzzy_match_example = fuzzyMatching(substring_1_positions, substring_2_positions, length_substring_1)

#Commented out for testing
# print(fuzzy_match_example) #(0,)

