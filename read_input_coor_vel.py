import numpy as np
import json
from constant import mas,autoan
class get_X_0(object):
    def __init__(self):
        self = self
    def get_init_coordinate(self,filename):
        op = open(filename,'r').read().splitlines()
        num = len(op)
        #print(num)
        X_0 = []
        symbol = []
        for symbol_coordinate in op:
            if symbol_coordinate.strip() != '':
                line_split_op = symbol_coordinate.split()
                for i in range(1,len(line_split_op)):
                    line_split_op[i] = float(line_split_op[i])
                #print(line_split_op[1:])
                X_0.append(line_split_op[1:])
                #print(line_split_op[0])
                symbol.append(line_split_op[0])

        return X_0,symbol
  

class get_input(object):
    def __init__(self):
        self = self
    def get_info_from_input(self,init_filename):
        op = open(init_filename,'r').read().splitlines()
        inputed_data = {}
        for keyword in op:
            if not len(keyword) or keyword.startswith('#'):
                continue
            if '=' in keyword:
                keyword = keyword.replace('=',' ')
            key_value  = keyword.split()
            inputed_data[key_value[0]] = key_value[1]
        
        return inputed_data


class get_v_0(object):
    def __init__(self):
        self = self
    def get_init_velocity(self,init_velocity_filename):
        op = open(init_velocity_filename,'r').read().splitlines()
        v_0 = []
        v = []
        for symbol_velocity in op:
            if symbol_velocity.strip() != '':
                line_split_op = symbol_velocity.split()
                for i in range(1,len(line_split_op)):
                    line_split_op[i] = float(line_split_op[i])
                v_0.append(line_split_op[1:])
        #print(v_0)
        return v_0

class para_data_X_v(object):
    def __init__(self):
        self = self
    def write_in_file(self,inputed_data,X_0,symbol,v_0):
        filename = 'tmp_file_para_all.txt'
        op = open(filename,'w')
        op.write('#Here\'s inputed_data \n')
        for key in inputed_data:
            op.write(key+'='+inputed_data[key])
            op.write('\n')
        op.write('#Here\'s Symbol and mass\n')
        op.write('symb = '+str(symbol))
        op.write('\n')
        for symb in symbol:
            op.write(symb+'='+str(mas[symb]))
            op.write('\n')
        op.write('#Here\'s X_0 \n')
        op.write('X_0'+'='+str(X_0))
        op.write('\n')
        op.write('#Here\'s v_0 \n')
        op.write('v_0'+'='+str(v_0))
        op.write('\n')


        op.close()
        return filename




if __name__ == '__main__':
    GX = get_X_0()
    X_0,symbol = GX.get_init_coordinate('coordinate.txt')
    G = get_input()
    inputed_data = G.get_info_from_input('input.inp')
    Gv = get_v_0()
    v_0 = Gv.get_init_velocity('velocity.txt') 
    Para_w = para_data_X_v()
    filename = Para_w.write_in_file(inputed_data,X_0,symbol,v_0)
   





