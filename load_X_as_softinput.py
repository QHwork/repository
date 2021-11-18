import numpy as np
from constant import autoan
class load_for_soft(object):
    def __init__(self):
        self = self
   
    def get_coordinates(self,X,intcycle):
        coordinates = np.array(X[intcycle],dtype = float)
        coordinates = coordinates*autoan
        return coordinates
         
    def writein_gjf(self,filename,coordinates,intcycle,num_of_eles,symb):
        op_old = open(filename+'.gjf').readlines()

        new_gjf_name = filename+str(intcycle+1) 
        op_new = open(new_gjf_name+'.gjf','w')
        linenu = 0
        linena = 0
        for i,line in enumerate(op_old):

            if line.strip() == '':
                linena += 1
            if linena == 2:
                linenu = i + 4
                break

        for i in range(linenu):
            op_new.write(op_old[i])
        for i in range(linenu,linenu+num_of_eles):
            op_new.write('{0:5}{1[0]:15.8f}{1[1]:15.8f}{1[2]:15.8f}\n'.format(symb[i-linenu],coordinates[i-linenu]))
        for i in range(linenu+num_of_eles,len(op_old)):
            op_new.write(op_old[i])
        op_new.close()
        return new_gjf_name
 

if __name__ == '__main__':
    X = [[[-0.00000000,0.00000000,0.21550200603661263],[-0.00000000,1.4755797251370055,-0.8620080241464505],[-0.00000000,-1.4755797251370055,-0.8620080241464505]]]
    intcycle = 0
    filename = 'model'
    num_of_eles = 3
    symb = ['H','O','H']
    W = load_for_soft()
    coordinates = W.get_coordinates(X,intcycle)
    #print(coordinates)