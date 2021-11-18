#! /bin/usr/python3
import os
import re
import json
import numpy as np
import hmmlearn.hmm as hmm
from constant import Bl
from constant import autoan

status = [1,0]
obs = [1,0]

n_status = len(status)
m_obs = len(obs)

start_prob = np.array([0.5,0.5])
transition_prob = np.array([[0.9999,0.0001],[0.0001,0.9999]])
emission_prob = np.array([[0.55,0.45],[0.45,0.55]])

model = hmm.MultinomialHMM(n_components=n_status)
model.startprob_ = start_prob
model.transmat_ = transition_prob
model.emissionprob_ = emission_prob


coor_all = open('tmp_X_V.json','r')
dic_X = json.load(coor_all)
para_all = open('tmp_paraall_json.json','r')
para = json.load(para_all) 
sym = para["symb"]
num_eles = np.loadtxt('num_sum')
sym = sym.split("'")
for i in sym:
    if i=="," or i=="[" or i=="]":
        sym.remove(i)
#print(sym)
a = []
# change here
Bl_graph_all = np.zeros((len(dic_X)//2,num_eles,num_eles))
for i in range(len(dic_X)//2):
    Xname = 'X{i}'
    X_i = np.array(dic_X[Xname.format_map(vars())])
    c = []
    Bl_ = []
    Bl_graph = []
    for j in range(len(X_i)):
        for k in range(len(X_i)):
            dis_ = X_i[j]-X_i[k]
            dis_ = np.linalg.norm(dis_)
            c.append(dis_)
            Bl_.append(sym[j]+'-'+sym[k])
    for j in range(len(Bl_)):
        if c[j]*autoan <= 1.4*Bl[Bl_[j]]/100:
            Bl_graph.append(1)
        else:
            Bl_graph.append(0)     

    Bl_graph = np.array(Bl_graph)
    Bl_graph = Bl_graph.reshape(len(sym),len(sym))
    # change here
    Bl_graph_all[i] = Bl_graph    
if (Bl_graph_all[0]==Bl_graph_all[-1]).all():
    cha =0
else:
    cha =1

for i in range(1,len(Bl_graph_all)):
    zero = np.zeros((len(Bl_graph_all[i]),len(Bl_graph_all[i])))
    d = Bl_graph_all[i]-Bl_graph_all[0]
    #print(d)
    if (d==zero).all():
        a.append(1)
    else:
        a.append(0)

a  = np.array(a)
print(a)
c = len(a)
a = a.reshape(c,1)
seen = a 
logprob,state = model.decode(seen,algorithm='viterbi')
logprob,state = model.decode(state.reshape((c,1)),algorithm='viterbi')
f_matrix_reaction = open('../Matrix_reaction','a')
print(state)       
if (state[-1]==state[0]) and (0 not in state):
    print('No reaction')
else:
    if 1 not in state:
        f_matrix_reaction.write(str(35)+'\n')
    for i in range(1,len(state)):
        if state[i]-state[i-1]!=0:
            f_matrix_reaction.write(str(i+1)+'\n')
    f_matrix_reaction.write('Reaction'+'\n')
