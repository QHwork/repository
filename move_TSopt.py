#! /bin/usr/python3
import os
import numpy as np
op = np.loadtxt('for_TS_forTS')
p = np.loadtxt('gjf_forTS')
p = np.sort(p)
TS = []
print(op)
if str(np.shape(op))=="()":
    print('op',op)
    TS.append('gmodel'+str(int(p[int(op)-1])-1+4)+'.gjf')
    TS.append('gmodel'+str(int(p[int(op)-1])-1+6)+'.gjf')
    TS.append('gmodel'+str(int(p[int(op)-1])-1+8)+'.gjf')
else:
    for i in op:
        print(int(i))
        print(int(p[int(i)-1]))
        TS.append('gmodel'+str(int(p[int(i)-1])-1+4)+'.gjf')
        TS.append('gmodel'+str(int(p[int(i)-1])-1+6)+'.gjf') 
        TS.append('gmodel'+str(int(p[int(i)-1])-1+8)+'.gjf')
opw = open('forTS_cp','w')
for i in TS:
    opw.write(i+'\n')
opw.close()
    


