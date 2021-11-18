import importlib

class save_update(object):
    def __init__(self):
        self = self
    def saveup(self,intcycle,X,V,Ek,num_of_eles,symb):
        a = importlib.import_module('saveas_ang')
        b = importlib.import_module('update_X_V')
        a.saveas_ang().writein_ang(intcycle,X,V,Ek,num_of_eles,symb)
        b.fresh_X_V().update_to_json(intcycle,X,V)
