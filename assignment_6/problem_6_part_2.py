"""
Players take turns contributing a letter to a word fragment when playing the game. The player loses if they create a real word unless the word is less than four letters. Another method of losing is to create a fragment that ensures no words can be made (i.e., ‘qz,’ there are no valid words where these two letters are contiguous).
15 October 2023
Aaman Bhandari

"""
import random

# -----------------------------------
# Helper functions
# (you don't need to understand this code)

wordlist_file = "words.txt"

def import_wordlist():
    """
    Imports a list of words from external file
    Returns a list of valid words for the game
    Words are all in lowercase letters
    """
    print("Loading word list from file...")
    with open(wordlist_file) as f:                        # call file, read file to list
        wordlist = [word.lower() for word in f.read().splitlines()]
    print("  ", len(wordlist), "words loaded.") 
    return wordlist


def into_dictionary(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# end of helper functions
# -----------------------------------

# Load the word dictionary by assignment the file name to 
# the wordlist variable 
wordlist = import_wordlist()

def play_ghost(word_list):
    """
    Implements the Ghost game for two human players.
    
    Inputs:
    - word_list: list                   ; The list of valid words
    
    Returns:
    - None
    """
    
    word_fragment = ""
    current_player = 1
    
    while True:
        # Display the current word fragment
        print(f"\nCurrent Word Fragment: '{word_fragment}'")
        print(f"Player {current_player}'s turn.")
        
        # Get player's input for letter and ensure lowercase
        letter = input("Enter a letter: ").lower()
        
        # Input validation: Ensure it's a single character and is alphabetical
        while not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single letter.")
            letter = input("Enter a letter: ").lower()
        
        # Append the letter to the word fragment
        word_fragment += letter
        
        # Check if the current word fragment forms a valid word
        if len(word_fragment) >= 4 and word_fragment in word_list:
            print(f"Player {current_player} loses! '{word_fragment}' is a valid word.")
            break
        
        # Check if the current word fragment cannot lead to any valid word
        is_valid_prefix = any(word.startswith(word_fragment) for word in word_list)
        if not is_valid_prefix:
            print(f"Player {current_player} loses! '{word_fragment}' cannot form a valid word.")
            break
        
        # Switch to the other player
        current_player = 3 - current_player  # Switches between 1 and 2
    
    return None
