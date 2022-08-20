import math
import os
import random
import re
import sys
# Complete the 'beautifulBinaryString' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
def beautifulBinaryString(b):
    # Write your code here
    i = 0
    c = 0
    while(len(b) > i):
        if(b[i:i+3] == '010'):
            i += 3
            c += 1
        else:
            i += 1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    fptr.write(str(result) + '\n')
    fptr.close()