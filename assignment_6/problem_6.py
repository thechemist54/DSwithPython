"""
Assignment 6 Problem 1: This game requires scores to be calculated from the words played. You need to design a solution to this problem using the function calc_word_score. This function should accept a string of lowercase letters as input (a word) and the maximum hand size. It will return a score. How a word arrives at this function or how this function fits in the big picture is outside the scope of this objective.

Assignment 6 Problem 2: Initially, a player is given a quasi-random set of letters. (There is a vowel-to-consonant ratio requirement.) The player’s hand may have more than one of a specific letter. The hand is stored in a dictionary to ensure that control can be maintained. For example, if the randomly chosen letters were e, e, m, t, s, w, and s, the dictionary would group them like terms. The dictionary that represents this hand is {e: 2, m: 1, t: 1, s: 2, w:1}. The data is represented this way for several reasons. Some of the reasons will be understood as you work through the code to complete different elements of this game. You'll get an error if you query for a key that isn’t in a dictionary. To get around this with modular programming, you will use the dictionary method .get(). However, letters in out. When you need to determine if a letter is in this dictionary, you can use this type of call: hand.get('a', 0). If the key is in the dictionary, it returns the value. If it doesn’t, it returns 0.

Assignment 6 Problem 3: You now have a large portion of this game complete. It’s now necessary to develop a method to test whether the word is valid. There are two criteria. The word must be in the word list. Additionally, the letters need to be in the player’s hand. Implement the function word_is_valid to return true if both criteria are met and false if either is not met. When you have finished solving this problem, use the testing file’s test_word_validity. Like the other problems, ensure that develop additional unit tests for any boundaries not assessed.

Assignment 6 Problem 4: The next step is to implement the ability for a user to play with a single hand. Update the function playing_hands to solve this problem. Don’t assume there are seven letters in the player’s hand. To see what you might find in the output from this function, see Figures 3, 4, and 5. This function connects several functions together. Read through the information provided in the skeleton to learn more about the requirements of this function. Make sure that you thoroughly test this function and functions interaction

Assignment 6 Problem 5: A game consists of one-to-many hands. There is one final function needed to complete this game. Delete the code that is present in that function and is not commented. Uncomment the code in the function start_game. No actual programming is necessary to solve this problem, just some deleting and comment toggling. If you would like, you can try to set the hand size to different values when you play the game. 

15 October 2023
Add the data this code was started or revised
Aaman Bhandari

"""

import random

vowels = 'aeiou'
not_vowels = 'bcdfghjklmnpqrstvwxyz'
letters_per_hand = 7

points_by_letter = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


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
    with open(wordlist_file) as f:                 # call file, read file to list
        wordlist = [word.lower() for word in f.read().splitlines()]
    print("  ", len(wordlist), "words loaded.") 
    return wordlist

def into_dictionary(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    sequence: str or list
    return: dictionary
    """
    # freqs: dictionary (values type: int)
    freq = {}
    for letter in sequence:
        freq[letter] = freq.get(letter, 0) + 1
    return freq


# end of helper functions
# -----------------------------------

# -----------------------------------
# Problem #1: Scoring a word

def calc_word_score(word, qty):
    """
    Returns the word score after word is validated.
    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all the letters in hand are used
    word: string (lowercase letters)
    returns: int >= 0
    """
    

    # Calculate the score using the points_by_letter dictionary
    score = sum(points_by_letter[letter] for letter in word)
    
    # If word length is equivalent to the maximum hand size, add an extra 50 points
    if len(word) == qty:
        score += 50
        
    return score

# # Let's test the function
# test_word = "example"
# test_qty = 7
# calc_word_score(test_word, test_qty)


# make sure you understand how this function works and what it does;
#    it will help with the work you have to do

def show_hand(hand):
    """
    Prints the letters in the player's hand
    For example:
       show_hand({'a':1, 'f':2, 'n':2, 'e':2})
    Prints something like:
       a f f n n e e
    The order of the letters is unimportant
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):   # calling the letters one by one from the dictionary
            print(letter, end = " "),   # print all on the same line
    print(" ")                          # print an empty line


# make sure you understand how this function works and what it does;
#    it will help with the work you have to do
def dealing_hands(qty):
    """
    Returns a random hand with qty lowercase letters for hand
    a third of letters are vowels
    the letters and letter frequencies are stored in a dictionary
    key = letter; value = frequency
    qty: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = qty // 3         # changed from divide to floor
    # collect the vowels
    for i in range(num_vowels):
        letter = vowels[random.randrange(0, len(vowels))]
        hand[letter] = hand.get(letter, 0) + 1
    # collect the consonants
    for i in range(num_vowels, qty):    
        letter = not_vowels[random.randrange(0, len(not_vowels))]
        hand[letter] = hand.get(letter, 0) + 1
        
    return hand

# -----------------------------------
# Problem #2: Update the hand by removing letters

def hand_update(hand, word):
    """
    After word played and validated, 
    removes letters in word from hand
    if hand has 2 a's & an 'a' was used,
    this updates hand to 1 'a'
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Convert the word to a dictionary of letter frequencies
    word_dict = into_dictionary(word)
    
    # For each letter in the word, subtract its frequency from the hand
    for letter, freq in word_dict.items():
        current_freq = hand.get(letter, 0)
        if current_freq > 0:
            hand[letter] = current_freq - freq
            
            # If the frequency of a letter becomes zero, remove it from the hand
            if hand[letter] == 0:
                del hand[letter]
    
    return hand

# -----------------------------------#
# Problem #3: Test the word validity

def word_is_valid(word, hand, word_list):
    """
    Returns boolean
    if all the letters in the word played are in the hand
    and
    if the word is in the wordlist
    returns true
    if either false, returns false
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase words
    """
    # Check if the word is in the word list
    if word not in word_list:
        return False
    
    # Convert the word into a dictionary of letter frequencies
    word_dict = into_dictionary(word)
    
    # Check if all letters of the word can be found in the player's hand
    for letter, freq in word_dict.items():
        if hand.get(letter, 0) < freq:
            return False
    
    return True

# -----------------------------------
# Problem #4: Playing a hand

def playing_hands(hand, word_list):
    """
    Allows the user to play the given hand, as follows:
    * hand shown
    * user can play a word from hand
    * invalid words are rejected with a message to player to play a different word
    * if valid word, remove letters from hand
    * if valid word scores word, adds score to total score
    * total score is shown to player after each valid word is scored
    * then the hand is shown, followed by asking user to play another word
    * hand is over when no remaining letters
    * user can stop game by entering a . instead of a word (the period)
    * if game ended, final score is shown
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    total_score = 0
    
    while True:
        # Display the user's hand
        print("\nCurrent Hand:", end=" ")
        for letter, freq in hand.items():
            print(letter * freq, end=" ")
        print("\n")
        
        # Prompt the user to provide a word
        word = input("Enter a word or a '.' to indicate that you are finished: ").lower()
        
        # If user wants to end the game
        if word == ".":
            print("Goodbye! Total score:", total_score, "points.")
            break
        
        # Check word validity
        if word_is_valid(word, hand, word_list):
            word_score = calc_word_score(word, len(hand))
            total_score += word_score
            print(f'"{word}" earned {word_score} points. Total: {total_score} points')
            hand = hand_update(hand, word)
            
            # Check if the hand is empty
            if not hand:
                print("\nAll letters are used. Total score:", total_score, "points.")
                break
        else:
            print("Invalid word. Please try again.")
    
    return None

# -----------------------------------
# Problem #5: Playing the game
# Make sure you understand how this code works
# 
def start_game(word_list):
    """
    Allow players an arbitrary number of hands
    ask user to enter 'n', 'r', or 'e' for the following options:
    * 'n': new random hand; when hand is played, user is asked to play 'n' or 'e' again
    * 'r': replay the previous hand
    * 'e': exit the game
    * if anything other than n, r, or e is entered, ask let user know the options again
    """
   
    
    # uncomment the following block of code once you've completed Problem #4
   
    while True:
       user_prompted = input('Enter n to start a new game, r to replay the last hand, or e to end game: ')
       if user_prompted == 'n':
           hand = dealing_hands(letters_per_hand)
           playing_hands(hand.copy(), word_list)
           print
       elif user_prompted == 'r':
           playing_hands(hand.copy(), word_list)
           print
       elif user_prompted == 'e':
           break
       else:
           print ("You did not choose from the options provided.")


# Used for entire session; this starts the game
#
if __name__ == '__main__':
    word_list = import_wordlist()
    start_game(word_list)
