#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    count=0
    a=set()
    while(n>0):
        if(n%2==1):
            count=count+1
            n=int(n/2)
            a.add(count)
        else:
            a.add(count)
            count=0
            n=int(n/2)
    
    print(max(a))
            