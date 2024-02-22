# Bianca Riebe - Prompt 3

import numpy as np

def offset_mean(array, target_mean):
    array_mean = np.mean(array)         # Find mean of original array
    offset = target_mean - array_mean   # Difference between target and original mean
    return array + offset               # Return the new array that has the new mean
