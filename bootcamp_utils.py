""" this file contains a bunch of codes to be reused"""

import numpy as np


#define function for ecdf
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)
    return x, y

    
