"""
Problem:

    A popular gameshow has a words round where contestants are required to guess at
    a word when it is written without any vowels in it.  For example, a clue might
    be "bldng" and the answer would be "building".

    The function 'clue' should take a word, and print out the corresponding clue
    for that word - the word minus any vowels.


Tests:

    >>> clue("building")
    bldng
    >>> clue("atmosphere")
    tmsphr
    >>> clue("perpendicular")
    prpndclr
    >>> clue("recipe")
    rcp

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def clue(word):

    new_word = ""
    count = 0
    
    for char in word:

         if char == "a":
             count = count + 1

         elif char == "e":
             count = count + 1

         elif char == "i":
             count = count + 1

         elif char == "o":
             count = count + 1

         elif char == "u":
             count = count + 1

         else:
             new_word = new_word + char

    print(new_word)
   
    
    

    
