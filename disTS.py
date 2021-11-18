#! /bin/usr/python3
import os
import numpy as np
from constant import Bl
from constant import autoan

#file_React = open('React','r').read().splitlines()
#file_React.remove('./for_TS')
all_TS = open('normal_TS','r').read().splitlines()
coor_all = np.loadtxt('coor_all')
sym = open('sym_all','r').read().splitlines()
print(len(sym))
coor_num = int(len(coor_all)/len(sym))
coor_all = coor_all.reshape((coor_num,len(sym),3))
coor_all_shape = np.shape(coor_all)
print(coor_all_shape)
Bl_graph_all = np.zeros((len(coor_all),len(sym),len(sym)))
for i in range(len(coor_all)):
    a = coor_all[i]
    c = []
    Bl_ = []
    Bl_graph = []
    for j in range(len(a)):
        for k in range(len(a)):
            b = a[j]-a[k]
            b = np.linalg.norm(b)
            c.append(b)
            Bl_.append(sym[j]+'-'+sym[k])
    for j in range(len(Bl_)):
        if c[j] <= 1.4*Bl[Bl_[j]]/100:
            #if Bl_[j] == 'C-O' or Bl_[j] == 'O-C':
            #if Bl_[j] == 'C-N' or Bl_[j] == 'N-C':
            Bl_graph.append(1)
        else:
            Bl_graph.append(0)
    Bl_graph = np.array(Bl_graph)
    Bl_graph = Bl_graph.reshape(len(sym),len(sym))
    
    Bl_graph_all[i] = Bl_graph

TSversion = [1]
os.system('''echo 'TS version 1' > TSversion''')
file_TS = open('TSversion','a')
TSversion_n = []
TSversion_n.append(Bl_graph_all[0])
file_TS.write(all_TS[0])
for i in range(1,len(Bl_graph_all)):
    for j in range(len(TSversion_n)):
        zero = np.zeros((len(Bl_graph_all[i]),len(Bl_graph_all[i])))
        a = Bl_graph_all[i]-TSversion_n[j]
        if (a==zero).all():
            print('Same Connect Graph'+all_TS[i]+' Version '+str(j+1))
            break
        else:
            if j==len(TSversion_n)-1:
                TSversion_n.append(Bl_graph_all[i])
                print('version new')
                file_TS.write('\nTS version '+str(len(TSversion_n)))
                file_TS.write(all_TS[i])

print(len(TSversion_n))
