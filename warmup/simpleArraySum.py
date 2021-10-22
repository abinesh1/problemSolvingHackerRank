##https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    return sum(ar)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()


## return reduce((lambda x, y: x + y), ar)