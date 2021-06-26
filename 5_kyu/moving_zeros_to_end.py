'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''
def move_zeros(array):
    zeros = []
    nonzero = []
    
    for i in range(len(array)):
        if array[i] != 0:
            nonzero.append(array[i])
        else:
            zeros.append(array[i])
            
    return (nonzero+zeros)