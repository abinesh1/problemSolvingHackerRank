#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    r = k%26
    enc = alpha[r:] + alpha[:r]
    d = {}
    res = ''
    for i, x in zip(alpha, enc):
        d[i] = x
    for c in s:
        if c.lower() in d.keys():
            if c.isupper():
                res += d[c.lower()].upper()
            else:
                res += d[c.lower()]
        else:
            res += c
    return res
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
