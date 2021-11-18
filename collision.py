#! /bin/usr/python3
import os
import math
import numpy as np
#from       import total_Ekc
from constant import mas,amu_to_au,autoan
 
total_Ekc = 0.37

sym1 = open('sym1','r').read().splitlines()
sym2 = open('sym2','r').read().splitlines()

total_m1 = 0
for i in range(len(sym1)):
    total_m1 += mas[sym1[i]]*amu_to_au

total_m2 = 0
for i in range(len(sym2)):
    total_m2 += mas[sym2[i]]*amu_to_au

plus_v1 = math.sqrt(2*total_Ekc/((total_m1**2)/total_m2+total_m1))
plus_v2 = math.sqrt(2*total_Ekc/((total_m2**2)/total_m1+total_m2))

