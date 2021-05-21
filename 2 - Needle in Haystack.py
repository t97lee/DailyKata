'''
8 kyu
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
'''

##code##

def find_needle(haystack):
    if "needle" in haystack:
        position = haystack.index("needle")
        return("found the needle at position ") + str(position)
