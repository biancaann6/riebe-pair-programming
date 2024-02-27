# Bianca Riebe - Prompt 3

import numpy as np

def offset_mean(array, target_mean):
    array_mean = np.mean(array)         # Find mean of original array
    offset = target_mean - array_mean   # Difference between target and original mean
    return array + offset               # Return the new array that has the new mean

#Looks good


#Test the function

def test():
    print(offset_mean([2, 4, 5, 1, 2], 5))
    print(offset_mean([1, 2], 7))
