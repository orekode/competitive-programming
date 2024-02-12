#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    test_1 = n % 2 == 0
    test_2 = n >= 2 and n <= 5
    test_3 = n > 20
    weird_test = test_1 and (test_2 or test_3)
    
    if weird_test:
        print("Not Weird")
    else:
        print("Weird")
