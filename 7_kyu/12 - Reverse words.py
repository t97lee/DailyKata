'''
7 kyu

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''
def reverse_words(text):
    new_words = text.split(' ')
    reverse = []
    for words in new_words:
        reverse.append(words[::-1])
        
    return ' '.join(reverse)