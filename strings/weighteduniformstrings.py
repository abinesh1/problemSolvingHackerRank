#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    d = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(1, 27):
        d[alpha[i-1]] = i
    weights = set()
    counter = 0
    for i in range(len(s)):
        if(i!=0 and s[i] == s[i-1]):
            counter += 1
        else:
            counter = 1
        weights.add(counter*d[s[i]])
    return ['Yes' if i in weights else 'No' for i in queries ]
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
