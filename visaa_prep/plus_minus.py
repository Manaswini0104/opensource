import math
import os
import random
import re
import sys
def plusMinus(arr):
    pos=0
    neg=0
    zeros=0
    for i in arr:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1
        elif i==0:
            zeros+=1
    total=len(arr)
    pos_ratio=pos/total
    neg_ratio=neg/total
    zero_ratio=zeros/total
    print(round(pos_ratio,6))
    print(round(neg_ratio,6))
    print(round(zero_ratio,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
