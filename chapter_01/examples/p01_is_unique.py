"""
Problem statment

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

# Example 1

def has_unique_chars(string):
    """
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
    """
    Returns True if a string has all unique characters, False otherwise.
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

"""
This algorithm works by comparing each character in the string
with all other characters in the string. If a match is found, 
the function immediately returns False, indicating that the string 
has duplicate characters. If no duplicates are found after comparing all 
pairs of characters, the function returns True.

This algorithm has a time complexity of O(n^2), where n is the length of the input string. 
If you have large input strings, this algorithm may not be efficient. In that case, you may want to consider
using a different algorithm or adding additional data structures to improve the time complexity.
"""

