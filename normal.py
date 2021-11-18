#! /bin/usr/python3 
import os
fp = open('for_route','r').read().splitlines()
not_normal = open('not_allNormal','r').read().splitlines()

for i in range(len(not_normal)):
    if not_normal[i] in fp:
        fp.remove(not_normal[i])
f = open('Normal','a')
for i in range(len(fp)):
    f.write(fp[i]+'\n')
f.close()
    

