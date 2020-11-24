##########################################################
#  Python module template for helper functions of your own (IAML Level 10)
#  Note that:
#  - Those helper functions of your own for Questions 1, 2, and 3 should be defined in this file.
#  - You can decide function names by yourself.
#  - You do not need to include this header in your submission.
##########################################################

import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

def mean(x):
    total = np.sum(x, axis=0)
    noOfRows = x.shape[0]
    return total/noOfRows

def Euclid(x1,x2):
    return np.sqrt(np.sum((x2 - x1)**2))