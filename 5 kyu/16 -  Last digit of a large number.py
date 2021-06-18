'''
5 kyu

Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a ** b.

Note that a and b may be very large!

'''
def last_digit(n1, n2):
    return pow(n1, n2, 10) #using modular arithmetic