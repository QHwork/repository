import numpy as np
import importlib
import sub_interface_json
from constant import fs_to_au
class read_to_DD(object):
    def __init__(self):
        self = self
    def select_needed_info(self,para_all):
        num_of_eles = int(para_all['num_of_eles'])
        intcycle = int(para_all['intcycle'])
        numcycle = int(para_all['numcycle'])
        softused = para_all['softused']
        filename = para_all['filename']
        symb = eval(para_all['symb'])
        X_0 = eval(para_all['X_0'])
        V_0 = eval(para_all['v_0'])
        X_0 = np.array(X_0,dtype = float)
        V_0 = np.array(V_0,dtype = float)
        X_0 = tuple(map(tuple,X_0))
        V_0 = tuple(map(tuple,V_0))
        X = []
        V = []
        X.append(X_0)
        V.append(V_0)
        dt = float(float(para_all['dt'])/fs_to_au)
        return symb,X_0,V_0,X,V,dt,num_of_eles ,intcycle,numcycle,filename,softused
    def load_new_json_to_trans(self,filename,intcycle):
        obj = sub_interface_json.load_json(filename)
        F = []
        #print(range(intcycle))
        if intcycle == 0:
            F.append(obj['F0'])
        else:
            for i in range(intcycle+1):
                #print(i)
                for j in obj:
                    #print(j)
                    if 'F'+str(i) == j:
                        #print(obj[j])
                        F.append(obj[j]) 
        return F
        
if __name__ =='__main__':
    filename = r'tmp/tmp_force_json.json'
    intcycle = 0
    Rdd = read_to_DD()
    F = Rdd.load_new_json_to_trans(filename,intcycle)
    #print(F)
 