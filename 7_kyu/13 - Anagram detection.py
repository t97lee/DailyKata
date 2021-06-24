'''
7 kyu

An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
'''
def is_anagram(test, original):
    for i in test and original:
        test_sorted = sorted(test.lower())
        org_sorted = sorted(original.lower())
    if test_sorted == org_sorted:
        return True
    else:
        return False 

is_anagram('apple','pale')