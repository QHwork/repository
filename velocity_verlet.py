#! /bin/usr/python3
import os
import math 
import time
import importlib
import numpy as np
from constant import mas,Bl,amu_to_au,autoan

class vel_ver(object):
    def __init__(self):
        self=self
    def sym(self):
        os.system('''`bash sym.sh`''')
        time.sleep(1)
        sym1 = open('sym1','r').read().splitlines()
        sym2 = open('sym2','r').read().splitlines()
        return sym1,sym2
    def velocity_half(self,V,intcycle,dt,num2):
        v = np.array(V[intcycle],dtype=float)
        v_half = v
        return v_half
    def coordinates(self,X,v_half,num2,dt,intcycle):
        x = np.array(X[intcycle-1],dtype=float)
        for i in range(num2):
            coor = x[i] + v_half*dt
            x[i] = coor
        x = tuple(x)
        X.append(x)
        return X
    def velocity(self,V,dt,intcycle,v_half,num2):
        v = np.array(V[intcycle-1],dtype=float)
        for i in range(num2):
            v_i = v_half
            v = v_i
        v = tuple(v)
        V.append(v)
        return V
    def move_to_center(self,region):
        
        os.system('''`bash mv_for_visual.sh`''')
        time.sleep(1)
        khf_coor = np.loadtxt('khf_coor.txt')
        khf_reaction_region_center = []
        x = 0
        y = 0
        z = 0
        
        for j in region:
            x += j[0]
            y += j[1]
            z += j[2]
        khf_reaction_region_center.append(x/len(region))
        khf_reaction_region_center.append(y/len(region))
        khf_reaction_region_center.append(z/len(region))
        khf_reaction_region_center = np.array(khf_reaction_region_center)
        np.savetxt('khf_reaction_region_center.txt',khf_reaction_region_center,fmt='%0.8f')
        for i in range(len(khf_coor)):
            khf_coor[i] = khf_coor[i] - khf_reaction_region_center
        
        khf_afmv = khf_coor
        return khf_afmv
    def move_to_surface(self,surface_point):
        os.system('''`bash get_coor2.sh`''')
        time.sleep(1)
        x_start = np.loadtxt('coor2')
        h2o_reaction_region_center = []
        x = 0 
        y = 0
        z = 0

        for i in x_start:
            x += i[0]
            y += i[1]
            z += i[2]
        h2o_reaction_region_center.append(x/len(x_start))
        h2o_reaction_region_center.append(y/len(x_start))
        h2o_reaction_region_center.append(z/len(x_start))
        h2o_reaction_region_center = np.array(h2o_reaction_region_center)
        np.savetxt('h2o_reaction_region_center.txt',h2o_reaction_region_center,fmt='%0.8f')
        for i in range(len(x_start)):
            x_start[i] = x_start[i] - h2o_reaction_region_center + surface_point
        h2o_afmv = x_start
        return h2o_afmv
    def simplest_check(self,Bl,region_label,khf_afmv,X,intcycle,numcycle,total_Ekc,dt,num1,num2,sym1,sym2,surface_point,surface_point_i,surface_point_list):
        total_m2 = 0
        for i in range(num2):
            total_m2 += mas[sym2[i]]*amu_to_au
        v_num = math.sqrt(2*total_Ekc/total_m2)*21.87
        a = np.linalg.norm(surface_point)
        #print(surface_point,a)
        v_start = -v_num*surface_point/a
        #print(v_start)
        #print(khf_afmv)
        #print(h2o_afmv)
        V = []
        v_start = tuple(v_start)
        V.append(v_start)
        while intcycle < numcycle:
            v_half = vv.velocity_half(V,intcycle,dt,num2)
            #print(v_half)
            intcycle +=1
            #print(intcycle)
            X = vv.coordinates(X,v_half,num2,dt,intcycle)
            coor = np.array(X[intcycle])
            #print(coor)
            i = 0
            j = 0
            while i < num1:
                while j < num2:
                    dis = np.linalg.norm(khf_afmv[i]-coor[j])
                    print(dis)
                    str_dis = sym1[i]+'-'+sym2[i]
                    #print(Bl[str_dis]/100)
                    if (dis <= 1.4*Bl[str_dis]/100) and (i not in region_label):
                        j = num2+1
                        i = num1+1
                        intcycle = numcycle+1
                    elif (dis <= 1.4*Bl[str_dis]/100) and (i in region_label):
                        surface_point_list.append(surface_point_i)
                        j = num2+1
                        i = num1+1
                        intcycle = numcycle+1
                    else:
                        j +=1
                        if j == 4:
                            break
                i +=1
                j = 0
                #print(i)
            if intcycle >= numcycle:
                break            
            else:
                i = 0
                j = 0
            V = vv.velocity(V,dt,intcycle,v_half,num2)
        #print(surface_point_list[-1])
        return surface_point_list 


if __name__ == '__main__':
    vv = vel_ver()
    num1=np.loadtxt('num1')
    num1 = int(num1)
    num2=np.loadtxt('num2')
    num2 = int(num2)
    sym1,sym2 = vv.sym()
    total_Ekc = 0.37 
    intcycle = 0
    dt = 0.5
    region = np.loadtxt('region') 
    region_label = [0,1,2,3] 
    numcycle = 200

    khf_afmv = vv.move_to_center(region)
    surface_points = np.loadtxt('xyz.txt')
    surface_point_list = []
    for i in range(len(surface_points)):

        X=[]
        h2o_afmv = vv.move_to_surface(surface_points[i])
        x_start = tuple(h2o_afmv)
        X.append(x_start)
    
        surface_point = surface_points[i]
        #print(len(surface_point))
        surface_point_i = i
    
        surface_point_list = vv.simplest_check(Bl,region_label,khf_afmv,X,intcycle,numcycle,total_Ekc,dt,num1,num2,sym1,sym2,surface_point,surface_point_i,surface_point_list)
    np.savetxt('5000points',surface_point_list,fmt='%0.8f')
