'''
7 kyu

Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
'''
def capitals(word):
    return [cap for (cap,count) in enumerate(word) if count.isupper()]
