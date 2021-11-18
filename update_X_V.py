
import sub_interface_json

class fresh_X_V(object):
    def __init__(self):
        self = self
    def update_to_json(self,intcycle,X,V):
       
        dict_X_V = {}
        for i in range(intcycle+1):
            Xi = tuple(map(tuple,X[i]))
            Vi = tuple(map(tuple,V[i]))
            dict_X_V['X'+str(i)] = Xi
            dict_X_V['V'+str(i)] = Vi
        filename = r'tmp/tmp_X_V.json'
        sub_to_json = sub_interface_json.dump_json(filename,dict_X_V)
     
        return filename
'''
if __name__ == '__main__':
    intcycle = 1
    X = 
    V = 
    Fxv = fresh_X_V()
    Fxv.update_to_json()
'''