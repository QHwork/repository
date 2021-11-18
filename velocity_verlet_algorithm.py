import numpy as np
import importlib
from constant import mas,amu_to_au,autoan

class vel_ver(object):
    def __init__(self):
        self = self
    def v_v_half_velocity(self,V,F,intcycle,dt,num_of_eles,symb):

        v = np.array(V[intcycle], dtype = float)
        f = np.array(F[intcycle], dtype = float)
        v_half = v
        for i in range(num_of_eles):
            mass = float(mas[symb[i]]*amu_to_au)
            v_i = v[i] + 0.5*dt*f[i]/mass
            v_half[i]=v_i
        return v_half
    def v_v_coordinates(self,X,F,v_half,symb,num_of_eles,dt,intcycle):
        x = np.array(X[intcycle-1], dtype = float)
        for i in range(num_of_eles):
            mass = float(mas[symb[i]]*amu_to_au)
            coor = x[i] + v_half[i]*dt
            x[i] = coor
        x = tuple(map(tuple,x))
        X.append(x)
        return X
    def v_v_velocity(self,V,F,dt,intcycle,v_half,num_of_eles,symb):

        v = np.array(V[intcycle-1], dtype = float)
        f = np.array(F[intcycle], dtype = float) 
        for i in range(num_of_eles):
            mass = float(mas[symb[i]]*amu_to_au)
            v_i = v_half[i] + dt*(f[i])/(2*mass)
            v[i]=v_i
        v= tuple(map(tuple, v))
        V.append(v)
        return V
    def v_v_kineticE(self,V,symb,intcycle):
        cal_Ek = np.array(V[intcycle],dtype = float)
        Ek = 0
        for i in range(len(cal_Ek)):
            v_i = list(cal_Ek[i])
            for j in range(len(v_i)):
                v_i[j] = float(v_i[j])
                Ek_every = (v_i[j])*(v_i[j])*mas[symb[i]]/2*amu_to_au
                Ek += np.sum(Ek_every)
        return Ek


if __name__=='__main__':
    X = [((1,0,0),(0,1,0),(0,0,1))]
    F = [((1,0,0),(0,1,0),(0,0,1)),((1,0,0),(0,1,0),(0,0,1))]
    V = [((1,0,0),(0,1,0),(0,0,1))]
    symb = ['H','O','H']
    num_of_eles = 3
    dt = 20
    intcycle = 0
    vv = vel_ver()
    v_half = vv.v_v_half_velocity(V,F,intcycle,dt,num_of_eles,symb)
    #print(v_half)
    X = vv.v_v_coordinates(X,F,v_half,symb,num_of_eles,dt,intcycle)
    V = vv.v_v_velocity(V,F,dt,intcycle,v_half,num_of_eles,symb)
    #print(V)
    Ek = vv.v_v_kineticE(V,symb,intcycle)
