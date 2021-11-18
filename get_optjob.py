#! /bin/usr/python3
import os
fp1 = open('Matrix_reaction','r').read().splitlines()
for i in range(len(fp1)):
    if 'Reaction' in fp1[i]:
        react1 = fp1[i-1]
        route1 = fp1[i-2].split('_')[0]
        route_f = '''`echo {route1} >> for_route`'''
        os.system(route_f.format_map(vars()))
        for j in range(3):
            react_f = int(react1)-(int(react1)%10)-10*j+1
            reactf = '''`echo {route1}/gmodel{react_f}.gjf >> for_run`'''
            os.system(reactf.format_map(vars()))
        for j in range(1,4):
            react_a = int(react1)-(int(react1)%10)+10*j+1
            reacta = '''`echo {route1}/gmodel{react_a}.gjf >> for_run`'''
            os.system(reacta.format_map(vars()))
 
