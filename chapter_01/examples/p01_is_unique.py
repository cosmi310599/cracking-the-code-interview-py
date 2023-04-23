# import unittest

"""
Problem statment

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

# Example 1

def has_unique_chars(string):
    """_summary_
    Check if string has more characters than the number 
    of unique characters in ASCII, the reason of this is because in 
    implementation of algorithms to determine if a string has all unique 
    characters is that there are only 128 unique characters in ASCII  character SET
    """
    
    if len(string) > 128:
        return False
    # Tis often used to create a boolean array with 128 elements, each initialized to False.    
    char_set = [False] * 128
    # Iterate through each character in the string
    for char in string:
        # Get the ASCII value of the character
        val = ord(char)
        # If the character has already been seen, return False
        if char_set[val]:
            return False
        # Otherwise, mark the character as seen in the array
        char_set[val] = True
    
    # If we make it through the string without finding a duplicate, return True
    return True

# Example 2

def has_unique_chars(s):
    """_summary_

    Args:
        s (str): The string to check for uniqueness.
        
    Returns:
        bool: True if the string has no repeated characters, False otherwise.
    
    This function checks if the input string `s` contains any repeated characters by iterating over
    all pairs of characters in the string and checking for equality. If a pair of equal characters is
    found, the function returns False. If no repeated characters are found, the function returns True.

    This algorithm has a time complexity of O(n^2), where n is the length of the input string. 
    If you have large input strings, this algorithm may not be efficient. 

    """
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True



# Example 3

def is_unique_bit_vector(string):
    """
    The function first checks if the length of the string is greater than 120, which is the max number of unique characters that can be
    represented using 7 bits (since ASCII characters are 7 bits wide), if string length is greater than 128 returns False.

    Initializes the `checker` variable to 0, which will be used to keep track of the characters that have been seen so far.
    Then iterates over each character in the string and performs the following:
        - By ord method the ascii value of the character is obtained
        - The function checks if the 'val' bit is already set in the cheacker variable by performing a bitwise AND operator between 
          checket and 1 << val, if the result of the biwise is greater than 0 means that the val is already in cheacker
        - If val bit is not already set in cheacker, the function sets the val bit in cheacker by performing a bitwise OR operator between cheacker
          and 1 << val
    """
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True



# TODO: UNIT TEST CLASS

# class TestHasUniqueChars(unittest.TestCase):

# if __name__ == '__main__':
    # unittest.main()