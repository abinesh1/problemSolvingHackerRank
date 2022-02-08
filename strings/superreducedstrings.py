#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    l = list(s)
    i = 0
    while i<len(l)-1:
        if(l[i] == l[i+1]):
            del l[i], l[i]
            if i!=0: i-=1
        else:
            i+=1
    if len(l) == 0:
        return 'Empty String'
    else:
        return ''.join(l)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()