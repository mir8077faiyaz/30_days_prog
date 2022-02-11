#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    ns=0
    for i in range (0,len(a)):
        for j in range (0,len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                ns+=1
    print("Array is sorted in",ns,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[len(a)-1])
    