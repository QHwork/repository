#! /bin/usr/python3
import os
fp = open('for_TS','r').read().splitlines()
a = []
c = []
e = []
for i in range(len(fp)):
    fp1 = fp[i].split('/')[0]
    a.append(fp1)
for i in range(len(a)-1):
    d = a[i]
    if d != a[i+1]:
        c.append(d)
c.append(a[-1])
print(c)
for i in fp:
    fp_log0 = i.split('/')[0]
    c_ = '''`tail -1 {i} >> {fp_log0}/chkNormal`'''
    os.system(c_.format_map(vars()))

for i in c:
    #c_ = '''`rm {i}/chkNormal`'''
    #os.system(c_.format_map(vars()))

    ci = i+'/chkNormal'
    c_i = open(ci,'r').read().splitlines()
    for j in c_i:
        if 'Normal' not in j:
            e.append(i)
            c.remove(i)
            break
    
print(e)                
fe = open('not_allNormal','a')
for i in e:
    fe.write(i+'\n')
for i in c:
    c_ = '''`cp constant.py {i}/`'''
    os.system(c_.format_map(vars())) 
    c_i = '''`cp distance_graph_matrix.py {i}/`'''
    os.system(c_i.format_map(vars()))
    #ci = '''`python3 {i}/distance_graph_matrix.py`'''
    #os.system(ci.format_map(vars()))

