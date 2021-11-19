#! /bin/usr/bash
import os
import math
import numpy as np

sym = open('sym','r').read().splitlines()
noH = []
for i in sym:
    if i!='H':
        noH.append(i)

fp = open('region_label','a')
if len(noH) <= 4:
    region_label = []
    for i in range(len(sym)):
        region_label.append(i)
else:
    NBO = np.loadtxt('NBO')
    NBO = list(NBO)
    CFF = np.loadtxt('CFF')
    CFF = list(CFF)
    NBO_p = []
    NBO_n = []
    NBO_pi = []
    NBO_ni = []
    for i in NBO:
        if i < 0:
            NBO_p.append(i)   
        if i > 0:
            NBO_n.append(i)

    NBO_p.sort(reverse=True)
    NBO_n.sort(reverse=True)
    for i in NBO_p:
        NBO_pi.append(NBO.index(i))
    for i in NBO_n:
        NBO_ni.append(NBO.index(i))
    for i in range(len(NBO_n)):
        NBO_n[i] = -NBO_n[i]

    NBO_p_top5 = []
    NBO_p_top5i = []
    for i in range(len(NBO_p)):
        if i == 0:
            NBO_p_top5.append(NBO_p[0])
            NBO_p_top5i.append(NBO_pi[0])
        else:
            ijk = 0
            for j in range(len(NBO_p_top5)):
                if (NBO_pi[i] == NBO_p_top5i[j]+1) or (NBO_pi[i] == NBO_p_top5i[j]-1):
                    ijk+=1
            if ijk==0:
                NBO_p_top5.append(NBO_p[i])
                NBO_p_top5i.append(NBO_pi[i])
        if len(NBO_p_top5) == 5:
            break

    NBO_n_top5 = []
    NBO_n_top5i = []
    for i in range(len(NBO_n)):
        if i == 0:
            NBO_n_top5.append(NBO_n[0])
            NBO_n_top5i.append(NBO_ni[0])
        else:
            ijk = 0
            for j in range(len(NBO_n_top5)):
                if (NBO_ni[i] == NBO_n_top5i[j]+1) or (NBO_ni[i] == NBO_n_top5i[j]-1):
                    ijk +=1
            if ijk == 0:
                NBO_n_top5.append(NBO_n[i])
                NBO_n_top5i.append(NBO_ni[i])
        if len(NBO_n_top5) == 5:
            break
    sum_3p = []
    sum_3n = []
    for i in range(5):
        sum_3p.append(abs(NBO[NBO_p_top5i[i]])+abs(NBO[NBO_p_top5i[i]+1])+abs(NBO[NBO_p_top5i[i]-1]))
        sum_3n.append(abs(NBO[NBO_n_top5i[i]])+abs(NBO[NBO_n_top5i[i]+1])+abs(NBO[NBO_n_top5i[i]-1]))
    for i in range(5):    
        sum_3p.append(abs(NBO[NBO_p_top5i[i]])+abs(NBO[NBO_p_top5i[i]-1])+abs(NBO[NBO_p_top5i[i]-2]))
        NBO_p_top5i.append(NBO_p_top5i[i]-1)
        sum_3p.append(abs(NBO[NBO_p_top5i[i]])+abs(NBO[NBO_p_top5i[i]+1])+abs(NBO[NBO_p_top5i[i]+2]))
        NBO_p_top5i.append(NBO_p_top5i[i]+1)
        sum_3n.append(abs(NBO[NBO_n_top5i[i]])+abs(NBO[NBO_n_top5i[i]-1])+abs(NBO[NBO_n_top5i[i]-2]))
        NBO_n_top5i.append(NBO_n_top5i[i]-1)
        sum_3n.append(abs(NBO[NBO_n_top5i[i]])+abs(NBO[NBO_n_top5i[i]+1])+abs(NBO[NBO_n_top5i[i]+2]))
        NBO_n_top5i.append(NBO_n_top5i[i]+1)
    list_3p = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    list_3n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    dic_p = {}
    dic_n = {}
    for i in range(15):
        dic_p[str(sum_3p[i])] = list_3p[i]
        dic_n[str(sum_3n[i])] = list_3n[i]
    sum_3p.sort(reverse=True)
    sum_3n.sort(reverse=True)
    sum_pn = []
    for i in range(15):
        sum_pn.append(sum_3p[i])
        sum_pn.append(sum_3n[i])
    sum_pn.sort(reverse=True)
    print(sum_pn)
    region_label_all = np.zeros((10,3))
    for i in range(10):
        if str(sum_pn[i]) in dic_p:
            region_label_all[i,0] = int(NBO_p_top5i[dic_p[str(sum_pn[i])]]-1)
            region_label_all[i,1] = int(NBO_p_top5i[dic_p[str(sum_pn[i])]])
            region_label_all[i,2] = int(NBO_p_top5i[dic_p[str(sum_pn[i])]]+1)
        if str(sum_pn[i]) in dic_n:
            region_label_all[i,0] = int(NBO_n_top5i[dic_n[str(sum_pn[i])]]-1)
            region_label_all[i,1] = int(NBO_n_top5i[dic_n[str(sum_pn[i])]])
            region_label_all[i,2] = int(NBO_n_top5i[dic_n[str(sum_pn[i])]]+1)

    region_label_all = list(region_label_all)
    for i in range(len(region_label_all)):
        region_label_all[i] = list(region_label_all[i])
            
    region_label = []
    for i in range(len(region_label_all)):
        region_label_all[i].sort(reverse=False)
        region_label_all[i] = list(map(int,region_label_all[i]))
    #print(region_label_all)
    for i in region_label_all:
        if i not in region_label:
            region_label.append(i)

    print(region_label)
    for_rm = []
    for i in region_label:
        for j in i:
            if sym[j]=='H':
                for_rm.append(i)
                break
    for i in for_rm:
        region_label.remove(i)
    print(region_label)
    CFF_sum3 = []
    CFF_sum3i = []
    itk = 0
    while itk in range(len(CFF)-2):
        if itk+2 <= len(CFF):
            CFF_sum3i.append(itk)
            CFF_sum3.append(CFF[itk]+CFF[itk+1]+CFF[itk+2])
            itk = itk + 1
        else:
            break
    list_CFF = []
    for i in range(len(CFF_sum3)):
        list_CFF.append(i)
    dic_CFF = {}
    for i in range(len(CFF_sum3)):
        dic_CFF[str(CFF_sum3[i])] = list_CFF[i]
    CFF_sum3.sort()
    listCFF = []
    for i in range(len(CFF_sum3)):
        listCFF_i = []
        listCFF_i.append(CFF_sum3i[dic_CFF[str(CFF_sum3[i])]]) 
        listCFF_i.append(CFF_sum3i[dic_CFF[str(CFF_sum3[i])]]+1)
        listCFF_i.append(CFF_sum3i[dic_CFF[str(CFF_sum3[i])]]+2)
        listCFF.append(listCFF_i)
    #print(region_label)
    #print(listCFF)
    for i in region_label:
        if (i in listCFF) and (listCFF.index(i)/len(listCFF) < 5):
            print('^_^')
        else:
            region_label.remove(i)

    

    ring_not = input('If there is benzene ring needed, plz input yes, or else, no:\n')
    if ring_not=='yes':
        ring = input('Plz input ring_label (list):\n')
        region_label.append(ring_label)
        
    for i in region_label:
        fp.write(str(i)+'\n')        

